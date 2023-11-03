from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField, SubmitField,BooleanField
from wtforms.validators import DataRequired, Length, Email, Optional, Regexp

class RegisterForm(FlaskForm):
    name = StringField('Nombre *',validators=[DataRequired(message="Nombre es obligatorio"),Length(max=40)],description="Nombre")
    last_name =  StringField('Apellido *', validators=[DataRequired(), Length(max=40)],description="Apellido")
    phone = StringField('Telefono *', validators=[DataRequired(),Regexp('^[67]\d{8}$',message="Numero no valido")],description="Telefono")
    email = StringField('Email *', validators=[Email(),Optional()],description="Email")
    number = IntegerField("Nº acompañantes",default=0,description="Acompañantes")
    child_menu = IntegerField("Nº menu infantil",default=0,description="Menu infantil")
    alergies = StringField("Alergias",validators=[Length(max=64)])
    bus = BooleanField("Bus (desde Loja)",description="Bus(desde Loja)")
    submit = SubmitField('Enviar')
