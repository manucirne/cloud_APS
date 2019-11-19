#!flask/bin/python
from flask import Flask, redirect, url_for, request
from flask_restful import Api
from tarefa_aps1 import TarefaPorId, Tarefas
import os

app = Flask(__name__)
api = Api(app)

ip_saida = os.environ["IP_REDIRECT"]

api.add_resource(TarefaPorId, '/tarefa/<int:id>')
api.add_resource(Tarefas, '/tarefa')

@app.route('/healthcheck')
def hc():
    return '',200


if __name__ == '__main__':
    app.run('0.0.0.0',port=5000)