from flask import Flask, request
from flask_restful import Resource

id_count = 1

app = Flask(__name__)
dados = {}


class TarefaPorId(Resource):

    def get(self, id): #mostra uma tarefa por id
        global dados
        if id in dados:
            return dados[id], 200
        return {'Erro':'Id inexistente!'},400    
    '/tarefa'

    def delete(self, id): #deleta uma tarefa por id
        global dados
        try:
            del dados[id]
        except KeyError:
            return {"Erro":"Id inexistente!"},400
        return {"Sucesso":"Arrasou!"},200

    def put(self, id):  #update de uma tarefa por id
        global dados
        if id in dados:
            dados[id] = {}
            dados[id] = request.get_json()
            return {"Sucesso":"Arrasou!"},200
        return {"Erro":"Id inexistente!"},400
        


class Tarefas(Resource):
    def post(self):   #criatarefa
        global dados
        global id_count
        dados[id_count] = request.get_json()
        id_count += 1
        return {"Sucesso":"Arrasou!"},200

    def get(self): #mostra todas as tarfeas
        global dados
        if len(dados) > 0:
            return dados, 200
        return {"Erro":"Não temos dados para mostrar"}, 400