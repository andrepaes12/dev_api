from flask_restful import Resource
from flask import request
import json

lista_habilidades = ['Python', 'Java', 'Flask', 'PHP']


class Habilidades(Resource):
    def get(self):
        return lista_habilidades

    def post(self):
        dados = json.loads(request.data)    #Postman POST: "Django"
        lista_habilidades.append(dados)
        return lista_habilidades


class SpecHabilidades(Resource):
    def delete(self, pos):
        habilidade = lista_habilidades[pos]
        lista_habilidades.pop(pos)
        return {'status': 'sucesso', 'mensagem': f'Registro de ID {habilidade} excluído!'}

    def put(self, pos):
        dados = json.loads(request.data)  # armazenar os dados recebidos por JSON (by Body - POSTMAN)
        lista_habilidades[pos] = dados
        return lista_habilidades[pos]
