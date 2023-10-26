from flask import Flask,render_template,url_for
from . import public_bp


@public_bp.route('/',methods=['GET'])
def index():
    print("hola")
    return render_template("index.html")