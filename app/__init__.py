from flask import Flask
from .public import public_bp
def create_app():
     
     app = Flask(__name__)
     app.config.from_object("config.DevConfig")
     #Import BluePrint for public part                                                         
     app.register_blueprint(public_bp)
    
     return app