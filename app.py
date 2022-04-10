from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost:5432/aluguel'
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Inquilino(db.Model):
    __tablename__ = 'inquilino'
    id = db.Column(db.Integer, primary_key=True)
    nome=db.Column(db.String())
    data_nascimento = db.Column(db.String())





if __name__ == '__main__':
    app.run(debug=True)
