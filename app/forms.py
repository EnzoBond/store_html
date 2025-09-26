from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired,ValidationError
from app.models import User

class CadForm(FlaskForm):
    def validate_user(self, check_user):
        user = User.query.filter_by(usuario=check_user.data).first()
        if user:
            raise ValidationError("Usuário ja exite!")
        
    def validate_email(self, check_email):
        email = User.query.filter_by(email=check_email.data).first()
        if email:
            raise ValidationError("Email já usado!")
        
    def validate_senha(self, check_senha):
        senha = User.query.filter_by(senha=check_senha.data).first()
        if senha:
            raise ValidationError("Senha já existe!")
        
    user = StringField(label='User: ', validators=[Length(min=2, max=30), DataRequired()])   
    email = StringField(label='Email: ', validators=[Email(), DataRequired()])
    senhaOG = PasswordField(label='Senha: ', validators=[Length(min=6), DataRequired()])
    senhaConf = PasswordField(label="Confirmação de senha: ", validators=[EqualTo('senhaOG'), DataRequired()])
    submit = SubmitField(label='Cadastrar')
    
class LoginForm(FlaskForm):
    user = StringField(label='User: ', validators=[DataRequired()])
    senhaOG = PasswordField(label='Senha: ', validators=[DataRequired()])
    submit = SubmitField(label='Entrar')