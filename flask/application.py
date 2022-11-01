'''
Created on 2022. 11. 1.

@author: DLIVE
'''
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello Flask2222222222"
