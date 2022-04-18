from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost:5432/aluguel'
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Inquilino(db.Model):
    __tablename__ = 'inquilino'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String())
    data_nascimento = db.Column(db.Date())


class Corretor(db.Model):
    __tablename__ = 'corretor'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String())
    data_nascimento = db.Column(db.Date())


class Imovel(db.Model):
    __tablename__ = 'imovel'
    id = db.Column(db.Integer, primary_key=True)
    logradouro = db.Column(db.String())
    cep = db.Column(db.String())
    bairro = db.Column(db.String())
    cidade = db.Column(db.String())


class Aluguel(db.Model):
    __tablename__ = 'aluguel'
    id = db.Column(db.Integer, primary_key=True)
    imovel_id = db.Column(db.Integer, db.ForeignKey('imovel.id'))
    inquilino_id = db.Column(db.Integer, db.ForeignKey('inquilino.id'))
    corretor_id = db.Column(db.Integer, db.ForeignKey('corretor.id'))


@app.route('/inquilino', methods=['GET', 'POST'])
def inquilino():
    if request.method == 'GET':
        inquilinos = Inquilino.query.all()
        results = [
            {
                "nome": inquilino.nome,
                "data_nascimento": inquilino.data_nascimento
            } for inquilino in inquilinos
        ]
        return {"count": len(results), "inquilinos": results}
    elif request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            inquilino = Inquilino(nome=data['nome'], data_nascimento=data['data_nascimento'])
            db.session.add(inquilino)
            db.session.commit()
            return {"mensagem": f"inquilino {inquilino.nome} criado com sucesso"}
        else:
            return {"erro": "o payload não está em formato json"}


@app.route('/inquilino/<id>', methods=['GET', 'PUT', 'DELETE'])
def inquilino_id(id):
    inquilino = Inquilino.query.get_or_404(id)
    if request.method == 'GET':
        response = {
            "nome": inquilino.nome,
            "data_nascimento": inquilino.data_nascimento
        }
        return {"mensagem": "ok", "inquilino": response}
    elif request.method == 'PUT':
        data = request.get_json()
        inquilino.nome = data['nome']
        inquilino.data_nascimento = data['data_nascimento']
        db.session.add(inquilino)
        db.session.commit()
        return {"mensagem": f"inquilino {inquilino.nome} atualizado com sucesso "}
    elif request.method == 'DELETE':
        db.session.delete(inquilino)
        db.session.commit()
        return {"mensagem": f"inquilino {inquilino.nome} deletado com sucesso "}


@app.route('/corretor', methods=['GET', 'POST'])
def corretor():
    if request.method == 'GET':
        corretores = Corretor.query.all()
        results = [
            {
                "nome": corretor.nome,
                "data_nascimento": corretor.data_nascimento
            } for corretor in corretores
        ]
        return {"count": len(results), "corretores": results}
    elif request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            corretor = Corretor(nome=data['nome'], data_nascimento=data['data_nascimento'])
            db.session.add(corretor)
            db.session.commit()
            return {"mensagem": f"corretor {corretor.nome} criado com sucesso"}
        else:
            return {"erro": "o payload não está em formato json"}


@app.route('/corretor/<id>', methods=['GET', 'PUT', 'DELETE'])
def corretor_id(id):
    corretor = Corretor.query.get_or_404(id)
    if request.method == 'GET':
        response = {
            "nome": corretor.nome,
            "data_nascimento": corretor.data_nascimento
        }
        return {"mensagem": "ok", "corretor": response}
    elif request.method == 'PUT':
        data = request.get_json()
        corretor.nome = data['nome']
        corretor.data_nascimento = data['data_nascimento']
        db.session.add(corretor)
        db.session.commit()
        return {"mensagem": f"corretor {corretor.nome} atualizado com sucesso "}
    elif request.method == 'DELETE':
        db.session.delete(corretor)
        db.session.commit()
        return {"mensagem": f"corretor {corretor.nome} deletado com sucesso "}


@app.route('/imovel', methods=['GET', 'POST'])
def imovel():
    if request.method == 'GET':
        imoveis = Imovel.query.all()
        results = [
            {
                "logradouro": imovel.logradouro,
                "cep": imovel.cep,
                "bairro": imovel.bairro,
                "cidade": imovel.cidade
            } for imovel in imoveis
        ]
        return {"count": len(results), "imoveis": results}
    elif request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            imovel = Imovel(logradouro=data['logradouro'], cep=data['cep'], bairro=data['bairro'],
                            cidade=data['cidade'])
            db.session.add(imovel)
            db.session.commit()
            return {"mensagem": f"imovel criado com sucesso"}
        else:
            return {"erro": "o payload não está em formato json"}


@app.route('/imovel/<id>', methods=['GET', 'PUT', 'DELETE'])
def imovel_id(id):
    imovel = Imovel.query.get_or_404(id)
    if request.method == 'GET':
        response = {
            "logradouro": imovel.logradouro,
            "cep": imovel.cep,
            "bairro": imovel.bairro,
            "cidade": imovel.cidade
        }
        return {"mensagem": "ok", "imovel": response}
    elif request.method == 'PUT':
        data = request.get_json()
        imovel.logradouro = data['logradouro']
        imovel.cep = data['cep']
        imovel.bairro = data['bairro']
        imovel.cidade = data['cidade']
        db.session.add(imovel)
        db.session.commit()
        return {"mensagem": f"imovel atualizado com sucesso "}
    elif request.method == 'DELETE':
        db.session.delete(imovel)
        db.session.commit()
        return {"mensagem": f"imovel deletado com sucesso "}


@app.route('/aluguel', methods=['GET', 'POST'])
def aluguel():
    if request.method == 'GET':
        alugueis = Aluguel.query.all()
        results = [
            {
                "imovel_id": aluguel.imovel_id,
                "inquilino_id": aluguel.inquilino_id,
                "corretor_id": aluguel.corretor_id
            } for aluguel in alugueis
        ]
        return {"count": len(results), "alugueis": results}
    elif request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            aluguel = Aluguel(imovel_id=data['imovel_id'], inquilino_id=data['inquilino_id'],
                              corretor_id=data['corretor_id'])
            db.session.add(aluguel)
            db.session.commit()
            return {"mensagem": f"aluguel criado com sucesso"}
        else:
            return {"erro": "o payload não está em formato json"}


@app.route('/aluguel/<id>', methods=['GET', 'PUT', 'DELETE'])
def aluguel_id(id):
    aluguel = Aluguel.query.get_or_404(id)
    if request.method == 'GET':
        response = {
            "imovel_id": aluguel.imovel_id,
            "inquilino_id": aluguel.inquilino_id,
            "corretor_id": aluguel.corretor_id
        }
        return {"mensagem": "ok", "aluguel": response}
    elif request.method == 'PUT':
        data = request.get_json()
        aluguel.imovel_id = data['imovel_id']
        aluguel.inquilino_id = data['inquilino_id']
        aluguel.corretor_id = data['corretor_id']
        db.session.add(aluguel)
        db.session.commit()
        return {"mensagem": f"aluguel atualizado com sucesso "}
    elif request.method == 'DELETE':
        db.session.delete(aluguel)
        db.session.commit()
        return {"mensagem": f"aluguel deletado com sucesso "}


if __name__ == '__main__':
    app.run(debug=True)
