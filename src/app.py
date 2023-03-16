from flask import Flask
from .routes import initalize_routes
from dotenv import load_dotenv
import os
load_dotenv()

app=Flask(__name__)

initalize_routes(app)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')