import mip
from itertools import product
from funcs import *

###############
# Parameters
###############

lechuga_name = ['lechuga'] * 2
lechuga_familia = ['lechuga'] * 2
lechuga_dias = [
"10/09/2021",
"17/09/2021",
]
lechuga_tiempo = [53] * 2
lechuga_camas = [3] + [2]
lechuga_precio = [1] * 2


espinaca_name = ['espinaca'] * 2
espinaca_familia = ['espinaca'] * 2
espinaca_dias = [
"1/09/2021",
"29/09/2021",
]
espinaca_tiempo = [61] * 2
espinaca_camas = [4] * 2
espinaca_precio = [1] * 2

cilantro_name = ['cilantro'] * 2
cilantro_familia = ['cilantro'] * 2
cilantro_dias = [
"10/09/2021",
"17/09/2021",
]
cilantro_tiempo = [65] * 2
cilantro_camas = [2] * 2
cilantro_precio = [1] * 2

acelga_name = ['acelga'] * 2
acelga_familia = ['acelga'] * 2
acelga_dias = [
"6/09/2021",
"2/02/2022",
]
acelga_tiempo = [90] * 2
acelga_camas = [3] * 2
acelga_precio = [1] * 2


perejil_name = ['perejil'] * 2
perejil_familia = ['perejil'] * 2
perejil_dias = [
"23/09/2021",
"8/12/2021",
]
perejil_tiempo = [139, 140]
perejil_camas = [1, 2]
perejil_precio = [1] * 2


cebollin_name = ['cebollin'] * 2
cebollin_familia = ['cebollin'] * 2
cebollin_dias = [
"20/09/2021",
"23/10/2021",
]
cebollin_tiempo = [85, 86]
cebollin_camas = [2] * 2
cebollin_precio = [1] * 2


mini_lechuga_name = ['mini_lechuga'] * 2
mini_lechuga_familia = ['lechuga'] * 2
mini_lechuga_dias = [
"5/09/2021",
"12/09/2021",
]
mini_lechuga_tiempo = [102, 101, ]
mini_lechuga_camas = [2] + [3]
mini_lechuga_precio = [1] * 2


betarraga_name = ['betarraga'] * 2
betarraga_familia = ['betarraga'] * 2
betarraga_dias = [
"30/09/2021",
"14/10/2021",
]
betarraga_tiempo = [82] * 2
betarraga_camas = [3] * 2
betarraga_precio = [1] * 2

kale_name = ['kale'] * 2
kale_familia = ['kale'] * 2
kale_dias = [
"10/09/2021",
"6/12/2021",
]
kale_tiempo = [130, 120]
kale_camas = [3] * 2
kale_precio = [1] * 2

puerro_name = ['puerro'] * 2
puerro_familia = ['puerro'] * 2
puerro_dias = [
"2/11/2021",
"16/11/2021",
]
puerro_tiempo = [127] * 2
puerro_camas = [1] * 2
puerro_precio = [1] * 2

tomate_beef_name = ['tomate_beef']
tomate_beef_familia = ['tomate']
tomate_beef_dias = [
"27/10/2021",
]
tomate_beef_tiempo = [205]
tomate_beef_camas = [5]
tomate_beef_precio = [1]

tomate_cherry_name = ['tomate_cherry']
tomate_cherry_familia = ['tomate']
tomate_cherry_dias = [
"6/11/2021",
]
tomate_cherry_tiempo = [195]
tomate_cherry_camas = [3]
tomate_cherry_precio = [1]

pepino_name = ['pepino'] * 2
pepino_familia = ['pepino'] * 2
pepino_dias = [
"18/10/2021",
"27/11/2021",
]
pepino_tiempo = [115] * 2
pepino_camas = [3] * 2
pepino_precio = [1] * 2

zuchini_name = ['zuchini'] * 2
zuchini_familia = ['zuchini'] * 2
zuchini_dias = [
"8/10/2021",
"18/12/2021",
]
zuchini_tiempo = [125, 110]
zuchini_camas = [2] * 2
zuchini_precio = [1] * 2

zanahoria_name = ['zanahoria'] * 2
zanahoria_familia = ['zanahoria'] * 2
zanahoria_dias = [
"30/09/2021",
"21/10/2021",
]
zanahoria_tiempo = [104, 99]
zanahoria_camas = [3] * 2
zanahoria_precio = [1] * 2

brasicas_name = ['brasicas'] * 2
brasicas_familia = ['brasicas'] * 2
brasicas_dias = [
"15/09/2021",
"22/09/2021",
]
brasicas_tiempo = [50] * 2
brasicas_camas = [2] * 2
brasicas_precio = [1] * 2

rucula_name = ['rucula'] * 2
rucula_familia = ['rucula'] * 2
rucula_dias = [
"15/09/2021",
"22/09/2021",
]
rucula_tiempo = [45] * 2
rucula_camas = [2] * 2
rucula_precio = [1] * 2

rabanito_name = ['rabanito'] * 2
rabanito_familia = ['rabanito'] * 2
rabanito_dias = [
"10/09/2021",
"17/09/2021",
]
rabanito_tiempo = [40] * 2
rabanito_camas = [1] * 2
rabanito_precio = [1] * 2

arveja_name = ['arveja'] * 2
arveja_familia = ['arveja'] * 2
arveja_dias = [
"5/09/2021",
"3/10/2021",
]
arveja_tiempo = [81] * 2
arveja_camas = [1] + [2]
arveja_precio = [1] * 2

#variables
semanas = 53
sectores = 14
camas = [10] * sectores
familias = ["lechuga", "espinaca", "cilantro", "acelga", "perejil", "cebollin", "betarraga", "kale", "puerro",
    "tomate", "pepino", "zuchini", "zanahoria", "brasicas", "rucula", "rabanito", "arveja"]

b_name = lechuga_name + espinaca_name + cilantro_name + acelga_name + perejil_name + cebollin_name\
    + mini_lechuga_name + betarraga_name + kale_name + puerro_name + tomate_beef_name + tomate_cherry_name\
    + pepino_name + zuchini_name + zanahoria_name + brasicas_name + rucula_name + rabanito_name + arveja_name


b_familia = lechuga_familia + espinaca_familia + cilantro_familia + acelga_familia + perejil_familia + cebollin_familia\
    + mini_lechuga_familia + betarraga_familia + kale_familia + puerro_familia + tomate_beef_familia + tomate_cherry_familia\
    + pepino_familia + zuchini_familia + zanahoria_familia + brasicas_familia + rucula_familia + rabanito_familia + arveja_familia

b_fechas = lechuga_dias + espinaca_dias + cilantro_dias + acelga_dias + perejil_dias + cebollin_dias\
    + mini_lechuga_dias + betarraga_dias + kale_dias + puerro_dias + tomate_beef_dias + tomate_cherry_dias\
    + pepino_dias + zuchini_dias + zanahoria_dias + brasicas_dias + rucula_dias + rabanito_dias + arveja_dias

b_tiempo = lechuga_tiempo + espinaca_tiempo + cilantro_tiempo + acelga_tiempo + perejil_tiempo + cebollin_tiempo\
    + mini_lechuga_tiempo + betarraga_tiempo + kale_tiempo + puerro_tiempo + tomate_beef_tiempo + tomate_cherry_tiempo\
    + pepino_tiempo + zuchini_tiempo + zanahoria_tiempo + brasicas_tiempo + rucula_tiempo + rabanito_tiempo + arveja_tiempo

b_camas = lechuga_camas + espinaca_camas + cilantro_camas + acelga_camas + perejil_camas + cebollin_camas\
    + mini_lechuga_camas + betarraga_camas + kale_camas + puerro_camas + tomate_beef_camas + tomate_cherry_camas\
    + pepino_camas + zuchini_camas + zanahoria_camas + brasicas_camas + rucula_camas + rabanito_camas + arveja_camas

b_precio = lechuga_precio + espinaca_precio + cilantro_precio + acelga_precio + perejil_precio + cebollin_precio\
    + mini_lechuga_precio + betarraga_precio + kale_precio + puerro_precio + tomate_beef_precio + tomate_cherry_precio\
    + pepino_precio + zuchini_precio + zanahoria_precio + brasicas_precio + rucula_precio + rabanito_precio + arveja_precio

delta = 28 // 7

SEMANAS = range(semanas)
SECTORES = range(sectores)
FAMILIAS = range(len(familias))
BLOQUES = range(len(b_name))


# date transformation
b_semanas = [date_to_week(fecha, custom_start='01/09/2021') for fecha in b_fechas]
b_tiempo = [num_to_week(tiempo) for tiempo in b_tiempo]

###############
# model
###############

#decision variables
model = mip.Model()
x = [[[[model.add_var(name=f"x({b},{s},{w},{c})", var_type=mip.BINARY)
    for c in range(camas[s])] for w in SEMANAS] for s in SECTORES] for b in BLOQUES]


#optimization function
model.objective = mip.maximize(mip.xsum(b_precio[b] * x[b][s][b_semanas[b]][c]
    for b in BLOQUES for s in SECTORES for c in range(camas[s])))


#################
# constraints
#################

# blocks must be planted at most once
for b in BLOQUES:
    model += mip.xsum(x[b][s][b_semanas[b]][c]
        for s in SECTORES for c in range(camas[s])
    ) <= 1

# blocks cannot be planted on another day than the one specified
for b in BLOQUES:
    model += mip.xsum(x[b][s][d][c]
        for s in SECTORES for d in b_semanas for c in range(camas[s])
        if d != b_semanas[b]
    ) == 0

# blocks cannot overlap
for (w, s) in product(SEMANAS, SECTORES):
    for c in range(camas[s]):
        model += mip.xsum(x[b][s][w_][c_]
            for b in BLOQUES for w_ in range(max(0, w+1-b_tiempo[b]), w+1) for c_ in range(max(0, c+1-b_camas[b]), c+1)
        ) <= 1

# blocks of the same botanical family cannot be planted in succession on the same bed
for (w, s, f) in product(SEMANAS, SECTORES, FAMILIAS):
    for c in range(camas[s]):
        model += mip.xsum(x[b][s][w_][c_]
            for b in BLOQUES for w_ in range(max(0, w+1-(b_tiempo[b]+delta)), w+1) for c_ in range(max(0, c+1-b_camas[b]), c+1)
            if b_familia[b] == familias[f]
        ) <= 1

# blocks must not be planted out of bounds
for s in SECTORES:
    model += mip.xsum(x[b][s][b_semanas[b]][c_]
        for b in BLOQUES for c_ in range(max(0, camas[s]-b_camas[b]+1), camas[s])
    ) == 0


#################
# solve
#################

model.optimize()


#################
# print results
#################
the_file = open('outputs/output.txt', 'w')
the_file.write("Schedule:\n")
for (b, s, w) in product(BLOQUES, SECTORES, SEMANAS):
    for c in range(camas[s]):
        if x[b][s][w][c].x >= 0.99:
            the_file.write(f"{b_name[b]} (family {b_familia[b]}): block {b}:\n")
            the_file.write(f"\tplanted at sector: ({s})\n")
            the_file.write(f"\tgrowth from day: ({b_fechas[b]} - {week_to_date(w+b_tiempo[b]-1, custom_start='01/09/2021')})\n")
            the_file.write(f"\tin beds: ({c} - {c+b_camas[b]-1})\n")
            the_file.write(f"\tprice: ({b_precio[b]})\n")
the_file.close()
print("all done")
