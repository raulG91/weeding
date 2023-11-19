from flask import Flask,render_template,url_for,flash,redirect
from . import public_bp
from .form import RegisterForm, ContactForm
from .model import Model


@public_bp.route('/',methods=['GET','POST'])
@public_bp.route("/register",methods=['GET','POST'])
def index():
    form = RegisterForm()
    if form.validate_on_submit():
        name = form.name.data
        last_name = form.last_name.data
        email = form.email.data
        phone = form.phone.data
        number = form.number.data
        child_menu = form.child_menu.data
        alergies = form.alergies.data
        bus = form.bus.data
        my_model = Model()
        my_model.insert_invitee(name,last_name,email,phone,str(number),str(child_menu),alergies,str(bus))
        flash("Se ha confirmado su asistencia")
        form.name.data = form.last_name.data = form.email.data = form.phone.data =  form.alergies.data = form.bus.data =""
        form.number.data = 0
        form.child_menu.data = 0
        return redirect(url_for('public.index'))
    else:
        return render_template("index.html",form = form)  

@public_bp.route("/contact",methods=['GET','POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        name = form.name.data
        last_name = form.last_name.data
        email = form.email.data
        phone = form.phone.data
        message = form.message.data
        my_model = Model()
        my_model.send_mail(name,last_name,email,phone,message)
        flash("Se ha enviado su mensaje")
        return redirect(url_for('public.contact'))
    else:
       return render_template("contact.html",form = form)  