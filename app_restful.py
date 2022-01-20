from flask import Flask, request
from flask_restful import Resource, Api
import json
from habilidades import Habilidades, SpecHabilidades  # from modulo[arquivo] import class_

app = Flask(__name__)
api = Api(app)

desenvolvedores = [
    {'id':0,
     'nome':'Andre',
     'habilidades':['Python', 'Flask']
     },
    {'id':1,
     'nome':'Paes',
     'habilidades':['PHP', 'Laravel']
     }
]


class Desenvolvedor(Resource):
    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = f'Desenvolvedor de ID {id} não existe.'
            response = {'status':'Error', 'mensagem':mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Favor entrar em contato com o ADMIN da API.'
            response = {'status': 'Error', 'mensagem': mensagem}
        return response

    def put(self, id):
        dados = json.loads(request.data)  # armazenar os dados recebidos por JSON (by Body - POSTMAN)
        desenvolvedores[id] = dados
        return dados

    def delete(self, id):
        desenvolvedores.pop(id)
        return {'status': 'sucesso', 'mensagem': f'Registro de ID {id} excluído!'}


class ListaDesenvolvedores(Resource):
    def get(self):
        return desenvolvedores

    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return desenvolvedores[posicao]


api.add_resource(Desenvolvedor, '/dev/<int:id>/')
api.add_resource(ListaDesenvolvedores, '/dev/')
api.add_resource(Habilidades, '/habilidades/')
api.add_resource(SpecHabilidades, '/habilidades/<int:pos>/')


if __name__ == '__main__':
    app.run(debug=True)

