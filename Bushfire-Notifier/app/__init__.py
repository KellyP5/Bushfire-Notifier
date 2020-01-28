from flask import Flask

app = Flask(__name__)

from app import detect_fires
from app import views
