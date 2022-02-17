from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
db = SQLAlchemy(app)

class user(db.Model):
    id = db.Column(db.integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email_address = db.Column(db.String(length=50), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)
    budget = db.Column(db.Integer(), nullable=False, default=1000)
    items = db.relationship('Item', backref='owned_user', lazy=True)

class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False,unique=True)
    description = db.Column(db.String(length=1000), nullable=False, unique=True)
    owner = db.Column(db.Integer(), db.Foreignkey('user.id'))

    def __repr__(self):
        return f'Item {self.name}'

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/market')
def market_page():
    items = Item.query.all()
    return render_template('market.html', items=items)

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)