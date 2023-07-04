from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from backend.db import db


def create_app(config_name):
    app=Flask(__name__)
    app.config.from_object(Config[config_name])
    Config[config_name].init_app(app)
    app.config.from_pyfile("../config.py")

    db.init_app(app)
    from backend.users.contoller import users
    from backend.Todos.controller import todos
   
   


    #IMPORTING BLUEPRINTS
    #from Backend.users.Controller import users

    #registering blue prints
    app.register_blueprint(users)
    app.register_blueprint(todos)


    return app