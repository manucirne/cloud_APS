from flask import Flask, request, jsonify
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
            "_id": str(id)
            }
        )
        return {"Dado":list(res)}, 200  

    def delete(self, id): #deleta uma tarefa por id
        global db
        qual = db.tarefas.delete(
            {
                "_id":str(id)
            }
        )
        return {"Sucesso":"Arrasou! tarefa deletada!"},200

    def put(self, id):  #update de uma tarefa por id
        global db
        res = request.get_json()
        filtro = {"_id":str(id)}
        qual = db.tarefa.find(
            {"_id":str(id)}
        )
        if qual == None:
            return {"Id":"inexistente"}, 200
        try:
            db.tarefas.update_one({
                "_id":str(id)
            },
                {"$set":{"texto":res["texto"],"mensagem":res["mensagem"]}}
            )
            return {"Sucesso":"Arrasou! Tarefa "},200
        except:
            return{"Envie campos com nomes texto e mensagem":"por favor!"}
        


class Tarefas(Resource):
    def post(self):   #criatarefa
        global db
        lista = list(db.ids.find())
        if lista == []:
            print("entrou no certo")
            db.ids.insert({
                "ultimo":0
            })
            data = request.get_json()
            data["_id"] = "0"
            db.tarefas.insert(
                data
                )
        else:
            id_count = lista[0]["ultimo"]
            db.ids.update({
                "ultimo":id_count
            },
            {
                "ultimo":id_count+1
            })
            data = request.get_json()
            data["_id"] = str(id_count)
            db.tarefas.insert(
                data
                )
        return {"Sucesso":"Arrasou!"},200

    def get(self): #mostra todas as tarefas
        global db
        dados = list(db.tarefas.find())
        print(dados)
        if dados == []:
            return {"Não existem dados" : "para serem mostrados"}, 200
        return {"Dados":dados}, 200