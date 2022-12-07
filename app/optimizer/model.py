import mip
import os
from datetime import date
from itertools import product
from .funcs import *


def get_params(sectores, blocks, unique_families):
    b_ids = []
    b_familias = []
    b_fechas = []
    b_tiempos = []
    b_camas = []
    b_precios = []

    # getting all the block attributes
    for item in blocks:
        b_ids.append(item['id'])
        b_familias.append(item['familia'])
        b_fechas.append(item['dia_plantacion'])
        b_tiempos.append(item['tiempo_crecimiento'])
        b_camas.append(item['camas_requeridas'])
        b_precios.append(item['precio'])

    # transforming days to weeks for the model
    the_custom_start = ''
    the_month = date.today().month
    if the_month < 9:
        the_custom_start = f'{date.today().year}-09-01'
    else:
        the_custom_start = f'{date.today().year + 1}-09-01'
    b_semanas = [date_to_week(fecha, custom_start=the_custom_start) for fecha in b_fechas]
    b_tiempos = [num_to_week(tiempo) for tiempo in b_tiempos]

    # getting all the sector attributes
    camas_por_sector = []
    sector_ids = []
    for item in sectores:
        sector_ids.append(item['id'])
        camas_por_sector.append(item['camas'])

    # returning all the params
    params = {
        'b_ids': b_ids,
        'b_familias': b_familias,
        'b_fechas': b_fechas,
        'b_semanas': b_semanas,
        'b_tiempos': b_tiempos,
        'b_camas': b_camas,
        'b_precios': b_precios,
        'camas_por_sector': camas_por_sector,
        'sector_ids': sector_ids,
        'delta': sectores[0]['delta'],
        'familias': unique_families,
    }
    return params

def get_constants(params):
    semanas = 53
    SECTORES = range(len(params['camas_por_sector']))
    week_delta = params['delta'] // 7
    SEMANAS = range(semanas)
    FAMILIAS = range(len(params['familias']))
    BLOQUES = range(len(params['b_ids']))

    constants = {
        'SECTORES': SECTORES,
        'SEMANAS': SEMANAS,
        'FAMILIAS': FAMILIAS,
        'BLOQUES': BLOQUES,
        'week_delta': week_delta,
    }
    return constants

def optimizer(sectores, blocks, unique_families):
    if not sectores or not blocks:
        return None
    params = get_params(sectores, blocks, unique_families)
    constants = get_constants(params)

    ###############
    # Parameters
    ###############

    print('------------------loading parameters...------------------')

    b_ids = params['b_ids']
    b_precio = params['b_precios']
    b_fechas = params['b_fechas']
    b_semanas = params['b_semanas']
    b_tiempos = params['b_tiempos']
    b_camas = params['b_camas']
    b_familias = params['b_familias']

    delta = params['delta']
    familias = params['familias']
    sector_ids = params['sector_ids']

    BLOQUES = constants['BLOQUES']
    SECTORES = constants['SECTORES']
    SEMANAS = constants['SEMANAS']
    FAMILIAS = constants['FAMILIAS']
    camas = params['camas_por_sector']


    ###############
    # model
    ###############

    print('------------------loading model...------------------')

    #decision variables
    model = mip.Model()
    x = [[[[model.add_var(name=f"x({b},{s},{w},{c})", var_type=mip.BINARY)
        for c in range(camas[s])] for w in SEMANAS] for s in SECTORES] for b in BLOQUES]


    #optimization function
    model.objective = mip.maximize(mip.xsum(b_camas[b] * b_precio[b] * x[b][s][b_semanas[b]][c]
        for b in BLOQUES for s in SECTORES for c in range(camas[s])))


    #################
    # constraints
    #################

    print('------------------loading constraints...------------------')
    print('------------------loading constraint 1...------------------')

    # blocks must be planted at most once
    for b in BLOQUES:
        model += mip.xsum(x[b][s][b_semanas[b]][c]
            for s in SECTORES for c in range(camas[s])
        ) <= 1

    print('------------------loading constraint 2...------------------')

    # blocks cannot be planted on another day than the one specified
    for b in BLOQUES:
        model += mip.xsum(x[b][s][d][c]
            for s in SECTORES for d in b_semanas for c in range(camas[s])
            if d != b_semanas[b]
        ) == 0

    print('------------------loading constraint 3...------------------')

    # blocks cannot overlap
    for (w, s) in product(SEMANAS, SECTORES):
        for c in range(camas[s]):
            model += mip.xsum(x[b][s][w_][c_]
                for b in BLOQUES for w_ in range(max(0, w+1-b_tiempos[b]), w+1) for c_ in range(max(0, c+1-b_camas[b]), c+1)
            ) <= 1

    print('------------------loading constraint 4...------------------')

    # blocks of the same botanical family cannot be planted in succession on the same bed
    for (w, s, f) in product(SEMANAS, SECTORES, FAMILIAS):
        for c in range(camas[s]):
            model += mip.xsum(x[b][s][w_][c_]
                for b in BLOQUES for w_ in range(max(0, w+1-(b_tiempos[b]+delta)), w+1) for c_ in range(max(0, c+1-b_camas[b]), c+1)
                if b_familias[b] == familias[f]
            ) <= 1

    print('------------------loading constraint 5...------------------')

    # blocks must not be planted out of bounds
    for s in SECTORES:
        model += mip.xsum(x[b][s][b_semanas[b]][c_]
            for b in BLOQUES for c_ in range(max(0, camas[s]-b_camas[b]+1), camas[s])
        ) == 0


    #################
    # solve
    #################

    print('------------------solving...------------------')

    model.optimize()


    #################
    # print results
    #################

    print('------------------printing results...------------------')

    the_string = ''
    the_string += '['
    for (b, s, w) in product(BLOQUES, SECTORES, SEMANAS):
        for c in range(camas[s]):
            if x[b][s][w][c].x >= 0.99:
                the_string += '{'
                the_string += f'"id": {b_ids[b]},'
                the_string += f'"sector": {sector_ids[s]},'
                the_string += f'"cama": {c}'
                the_string += '},'

    the_string = the_string[:-1]
    the_string += ']'
    the_file = open('outputs/output.json', 'w')
    the_file.write(the_string)
    the_file.close()
    print("all done")

    return '/app/outputs/output.json'
