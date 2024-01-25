from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuração do banco de dados (MySQL neste exemplo)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:B35EbBCG1cb656b146gcBfF22hADbFe6@roundhouse.proxy.rlwy.net:13366/railway'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Modelo da tabela
class Pessoas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)


# Rota para verificar se o nome existe na tabela
@app.route('/api/verificar_nome', methods=['POST'])
def verificar_nome():
    # Obtém o nome da requisição
    nome = request.json.get('nome')

    # Verifica se o nome existe na tabela
    pessoa_existente = Pessoas.query.filter_by(nome=nome).first()

    # Responde com True se o nome existir, False caso contrário
    resposta = {'existe': pessoa_existente is not None}
    return jsonify(resposta)


if __name__ == '__main__':
    # Inicia o servidor Flask
    app.run()
