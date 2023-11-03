from flask import Flask,render_template,url_for
from . import public_bp
from .form import RegisterForm
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
        return render_template("register.html",form = form) 
    else:
        return render_template("index.html",form = form)  


  