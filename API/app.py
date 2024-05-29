# Aplicação....: API Flask
# Objetivo.....: API para CRUD de livros
# URL Base.....: localhost
# Endpoints....: localhost/livros    (GET)
#                localhost/livros    (POST)
#                localhost/livros/id (GET)
#                localhost/livros/id (PUT)
#                localhost/livros/id (DELETE)
# Recursos.....: Livros

from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {'id': 1, 'título': 'Livro 1', 'autor': 'Autor livro 1'},
    {'id': 2, 'título': 'Livro 2', 'autor': 'Autor livro 2'},
    {'id': 3, 'título': 'Livro 3', 'autor': 'Autor livro 3'},
    {'id': 4, 'título': 'Livro 4', 'autor': 'Autor livro 4'},
    {'id': 5, 'título': 'Livro 5', 'autor': 'Autor livro 5'},
]

# Consultar (todos)


@app.route('/livros', methods=['GET'])
def obter_livros():
    return jsonify(livros)

# Consultar (por id)


@app.route('/livros/<int:id>', methods=['GET'])
def obter_livro_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)

# Editar (por id)


@app.route('/livros/<int:id>', methods=['PUT'])
def editar_livro_id(id):
    alteracao = request.get_json()
    for i, livro in enumerate(livros):
        if livro.get('id') == id:
            livros[i].update(alteracao)
            return jsonify(livros[i])

# Criar


@app.route('/livros', methods=['POST'])
def criar_livro():
    novo = request.get_json()
    livros.append(novo)
    return jsonify(livros)

# Excluir (por id)


@app.route('/livros/<int:id>', methods=['DELETE'])
def excluir_livro_id(id):
    for i, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[i]
            return jsonify(livros)


app.run(port=5000, host='localhost', debug=True)
