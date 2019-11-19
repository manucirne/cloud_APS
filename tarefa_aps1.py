from flask import Flask, request
from flask_restful import Resource
import pymongo
from pymongo import MongoClient
import os

id_count = 1

app = Flask(__name__)
dados = {}

ip_banco = os.environ["IP_BANCO"]


def get_db(ip_banco):
    client = MongoClient(ip_banco,27017)
    db = client.app_manu
    return db

db = get_db(ip_banco)


class TarefaPorId(Resource):

    def get(self, id): #mostra uma tarefa por id
        res = db.tarefas.find(
            {
            "_id": id
            }
        )
        return list(res), 200  

    def delete(self, id): #deleta uma tarefa por id
        global db
        qual = db.tarefas.delete(
            {
                "_id":id
            }
        )
        return {"Sucesso":"Arrasou! tarefa deletada!"},200

    def put(self, id):  #update de uma tarefa por id
        global db
        res = request.get_json()
        res["id_"] = id
        db.tarefas.update_one({
            '_id':id
        },
            res
        )
        return {"Sucesso":"Arrasou! Tarefa "},200
        


class Tarefas(Resource):
    def post(self):   #criatarefa
        global db
        lista = list(db.ids.find())
        id_count = lista[0]["ultimo"]
        if lista == []:
            db.ids.insert({
                "ultimo":0
            })
        else:
            db.ids.update({
                "ultimo":id_count
            },
            {
                "ultimo":id_count+1
            })
        db.tarefas.insert({
            str(id_count):request.get_json()
            })
        return {"Sucesso":"Arrasou!"},200

    def get(self): #mostra todas as tarefas
        global db
        dados = db.tarefas.find()
        return list(dados), 200