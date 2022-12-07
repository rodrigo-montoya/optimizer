from flask import Flask, render_template, request, jsonify
from optimizer.model import get_params, get_constants, optimizer

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def controller():
    if request.method == 'POST':
        json_data=request.get_json()
        blocks = []
        unique_families = []
        for item in json_data['bloques']:
            block = {
                'id': item['id'],
                'familia': item['familia_botanica'],
                'dia_plantacion': item['dia_plantacion'],
                'tiempo_crecimiento': item['tiempo_crecimiento'],
                'camas_requeridas': item['camas_requeridas'],
                'precio': item['precio'],
            }
            blocks.append(block)
            if item['familia_botanica'] not in unique_families:
                unique_families.append(item['familia_botanica'])
        sectores = json_data['sectores']

        output_path = optimizer(sectores, blocks, unique_families)
        if output_path:
            # output_path = '/app/outputs/output.json'
            file = open(output_path, 'r')
            content = file.read()
            return jsonify(content)
        else:
            return jsonify("[]")

    elif request.method == 'GET':
        data = {}
        data["key1"] = "value1"
        data["key2"] = "value2"

        return render_template('index.html', data=data)
