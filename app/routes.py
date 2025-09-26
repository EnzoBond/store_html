from app import app
from flask import render_template, redirect, url_for, flash
from app.models import Item, User
from app.forms import CadForm, LoginForm
from app import db
from flask_login import login_user, logout_user

@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/produtos')
def product_page():
    itens = Item.query.all()
    return render_template('product.html', itens = itens)

@app.route('/cadastro', methods=['GET', 'POST'])
def cad_page():
    form = CadForm()
    if form.validate_on_submit():
        usuario = User(
            usuario = form.user.data,
            email = form.email.data,
            senhaCrip = form.senhaOG.data
        )
        
        db.session.add(usuario)
        db.session.commit()
        return redirect(url_for('product_page'))
    
    if form.errors != {}:
        for err in form.errors.values():
            flash(f'Error ao cadastrar usuário {err}', category='danger')
    return render_template('cad.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        user_logged = User.query.filter_by(usuario = form.user.data).first()
        
        if user_logged and user_logged.converter_senha(senha_texto_claro=form.senhaOG.data):
            login_user(user_logged)
            flash("Sucesso! User Logado Com Sucesso!", category='success')
            return redirect(url_for('product_page'))
        else:
            flash("Usuario ou senha estão incorretos! Tente Novamente", category='danger')
    return render_template('login.html', form=form)

@app.route('/logout', methods=['GET', 'POST'])
def logout_page():
    logout_user()
    flash('Você deslogou da sua conta', category='info')
    return redirect(url_for("home_page"))

@app.route('/test')
def test_page():
    users = User.query.all()
    return render_template('test.html')