from flask import Flask

#initialize app
app = Flask(__name__, instance_relative_config=True)


#load views
from app import views


#load config file
app.config.from_object('config')

