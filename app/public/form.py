from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField, SubmitField,BooleanField,TextAreaField
from wtforms.validators import DataRequired, Length, Email, Optional, Regexp

class RegisterForm(FlaskForm):
    name = StringField('Nombre *',validators=[DataRequired(message="Nombre es obligatorio"),Length(max=40)],description="Nombre")
    last_name =  StringField('Apellido *', validators=[DataRequired(), Length(max=40)],description="Apellido")
    phone = StringField('Telefono *', validators=[DataRequired(),Regexp('^[67]\d{8}$',message="Numero no valido")],description="Telefono")
    email = StringField('Email *', validators=[Email(message="Email incorrecto"),Optional()],description="Email")
    number = IntegerField("Nº acompañantes",default=0,description="Acompañantes")
    child_menu = IntegerField("Nº menu infantil",default=0,description="Menu infantil")
    alergies = StringField("Alergias",validators=[Length(max=64)])
    bus = BooleanField("Bus (desde Loja)",description="Bus(desde Loja)")
    submit = SubmitField('Enviar')
class ContactForm(FlaskForm):
   name = StringField('Nombre *',validators=[DataRequired(message="Nombre es obligatorio"),Length(max=40)],description="Nombre")
   last_name =  StringField('Apellido *', validators=[DataRequired(), Length(max=40)],description="Apellido")
   email = StringField('Email *', validators=[Email(message="Email incorrecto"),Optional()],description="Email")
   message = TextAreaField('Mensaje', validators=[DataRequired(),Length(max=255)])
   submit = SubmitField('Enviar')