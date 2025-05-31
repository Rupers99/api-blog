from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = 'ASD123'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Silva.5014@db.ixozgvlfpnkgjzngonkl.supabase.co:5432/postgres'

db = SQLAlchemy(app)
db:SQLAlchemy

class Postagem(db.Model):
    __tablename__ = 'postagem'
    id_postagem = db.Column(db.Integer, primary_key=True)
    Titulo = db.Column(db.String)
    id_autor = db.Column(db.Integer, db.ForeignKey('autor.id_autor'))

class Autor(db.Model):
    __tablename__ = 'autor'
    id_autor = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String)
    email = db.Column(db.String)
    senha = db.Column(db.String)
    admin = db.Column(db.Boolean)
    postagens = db.relationship('Postagem')

def inicializar_banco():
    with app.app_context():
        db.drop_all()
        db.create_all()

        autor = Autor(nome='Luciano', email='luciano@gmail.com', 
                      senha='12345', admin=True)
        
        db.session.add(autor)
        db.session.commit()


if __name__ == '__main__':
    inicializar_banco()