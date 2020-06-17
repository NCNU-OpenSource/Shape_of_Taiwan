import flask
import logging
from flask import jsonify, request, render_template
import json

app = flask.Flask(__name__)
app.config["DEBUG"] = False
app.config["JSON_AS_ASCII"] = False
format_config = '%(asctime)s - %(levelname)s - %(message)s'
logging.basicConfig(format=format_config, level=logging.INFO)
logger = logging.getLogger()

@app.route('/getData', methods=['GET'])
def getData() :
    with open('./static/data.json', 'r', encoding='utf8') as f :
        return jsonify(json.load(f))

@app.route('/updateData', methods=['GET'])
def updateData():
    if 'zh_CN' in request.args :
        if request.args['zh_CN'] == '' :
            return "Error: Form format error"
        else :
            key = request.args['zh_CN']
            if 'zh_TW' in request.args and 'zh_US' in request.args :
                zh_TW = request.args['zh_TW']
                zh_US = request.args['zh_US']
            else :
                return "Error: Form format error"
    else :
        return "Error: Form format error"
    data = None
    with open('./static/data.json', 'r', encoding='utf8') as f :
        data = json.load(f)
        data[key] = {
            "zh_TW": zh_TW,
            "zh_US": zh_US
        }
    with open('./static/data2.json', 'w', encoding='utf8') as f :
        json.dump(data, f, ensure_ascii=False)
    return "Success"


if __name__ == "__main__":
    app.run()