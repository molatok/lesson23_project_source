import os

from flask import Flask, request
from func import *

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")


@app.route("/perform_query", methods=["POST"])
def perform_query():
    storage = ''
    data = request.json
    cmd1 = data['cmd1']
    value1 = data['value1']
    cmd2 = data['cmd2']
    value2 = data['value2']
    file_name = data['file_name']

    if file_name is None:
        return "Файл не указан", 400
    else:
        if (cmd1 or cmd2) is None:
            return "В запросе отсутствуют данные", 400

    file_path = os.path.join(DATA_DIR, file_name)

    if not os.path.exists(file_path):
        return "Файл не найден", 400

    with open(file_path, 'r') as data:
        if cmd1 == 'filter':
            storage = filter(data, value1)
        elif cmd1 == 'unique':
            storage = unique(data)
        elif cmd1 == 'sort':
            storage = sort(data, value1)
        elif cmd1 == 'limit':
            storage = limit(data, value1)
        elif cmd1 == 'map':
            storage = map(data, value1)
        if cmd2 == 'filter':
            return filter(storage, value2)
        elif cmd2 == 'unique':
            return unique(storage)
        elif cmd2 == 'sort':
            return sort(storage, value2)
        elif cmd2 == 'limit':
            return limit(storage, value2)
        elif cmd2 == 'map':
            return map(storage, value2)

