from flask import Flask, jsonify, request
import json

app = Flask(__name__)

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

#retorna um Dev pelo ID, tbm altera e deleta um Dev
@app.route('/dev/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = f'Desenvolvedor de ID {id} não existe.'
            response = {'status':'Error', 'mensagem':mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Favor entrar em contato com o ADMIN da API.'
            response = {'status': 'Error', 'mensagem': mensagem}
        return jsonify(response)
    elif request.method == 'PUT':
        dados = json.loads(request.data) #armazenar os dados recebidos por JSON (by Body - POSTMAN)
        desenvolvedores[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'status':'sucesso', 'mensagem':f'Registro de ID {id} excluído!'})


#lista todos os Dev e permite add um novo Dev
@app.route('/dev/', methods=['POST', 'GET'])
def lista_desenvolvedores():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return jsonify(desenvolvedores[posicao])
    elif request.method == 'GET':
        return jsonify(desenvolvedores)


if __name__ == '__main__':
    app.run(debug=True)