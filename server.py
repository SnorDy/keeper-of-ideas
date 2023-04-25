from flask import Flask, jsonify, request
import json

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
    with open('/home/Snordy/mysite/data.json') as file:
        file = json.load(file)
        return jsonify(file)


@app.route('/post', methods=['POST'])
def post():
    req = request.json
    with open('/home/Snordy/mysite/data.json', 'w') as file:
        file.seek(0, 0)
        json.dump(req, file, ensure_ascii=False)
    return jsonify({})
