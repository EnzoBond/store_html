from app import app
from flask import render_template
from app.models import Item, User

@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/produtos')
def product_page():
    itens = Item.query.all()
    return render_template('product.html', itens = itens)

@app.route('/cadastro')
def cad_page():
    return render_template('')

@app.route('/test')
def test_page():
    users = User.query.all()
    return render_template('test.html')