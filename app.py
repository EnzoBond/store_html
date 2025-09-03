from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/produtos')
def product_page():
    itens = [
        {'id':1, 'nome':'Celular', 'cod_barra':'23456789','preco':1200},
        {'id':2, 'nome':'Notebook', 'cod_barra':'35488654','preco':3500},
        {'id':3, 'nome':'Teclado', 'cod_barra':'56488654','preco':120},
        {'id':4, 'nome':'Monitor', 'cod_barra':'235465564','preco':800},
    ]
    return render_template('product.html', itens = itens)