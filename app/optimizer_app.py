from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def controller():
    if request.method == 'POST':
        the_thing=request.form.get('the_thing')
        json_data=request.get_json()
        return render_template('index.html', the_thing=the_thing, json_data=json_data)
    elif request.method == 'GET':
        data = {}
        data["key1"] = "value1"
        data["key2"] = "value2"

        return render_template('index.html', data=data)
