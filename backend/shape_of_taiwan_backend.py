import flask
import logging
from flask import jsonify, request, render_template
import json
# jieba
import jieba
jieba.set_dictionary('../static/file/dict.txt.big')
# import jieba_tw
import json

app = flask.Flask(__name__)
app.config["DEBUG"] = False
app.config["JSON_AS_ASCII"] = False
format_config = '%(asctime)s - %(levelname)s - %(message)s'
logging.basicConfig(format=format_config, level=logging.INFO)
logger = logging.getLogger()

@app.route('/getData', methods=['GET'])
def getData() :
    def get_result_json(): # private, 傳進網頁內容，return 比對到 網頁 與 key 的
        # 資料準備
        content = open('../static/file/web_content_demo.txt', 'r', encoding='utf8').read() # request - web content
        ch_dict_file = open('../static/file/data.json','r',encoding='utf8') # zh_CH.json
        ch_json_array = json.load(ch_dict_file)

        # 切分收到內容
        words = jieba.cut(content, cut_all=False) # 不要把所有可能的結果都列出來

        result_json = dict()
        for word in words: # 每個斷詞
            try: # 比對 ch_json_array[ch_key]
                result_json[word] = ch_json_array[word]
            except KeyError:
                continue

        with open('../static/file/result_data.json', 'w', encoding='UTF-8') as f:
            f.write(str(json.dumps(result_json, ensure_ascii=False)))
        with open('../static/file/result_data.json', 'r', encoding='UTF-8') as f:
            return jsonify(json.load(f))

    return get_result_json()


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