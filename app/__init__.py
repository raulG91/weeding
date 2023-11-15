from flask import Flask
from .public import public_bp
from flask_mail import Mail,Message
def create_app():
     
     app = Flask(__name__)
     app.config.from_object("config.ProdConfig")
     #Import BluePrint for public part                                                         
     app.register_blueprint(public_bp)
     email_object = Mail(app)
     #email.init_mail(app)
    
     return app