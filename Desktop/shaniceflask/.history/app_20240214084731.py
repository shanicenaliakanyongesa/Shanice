from flask import *
app=Flask(__name__)

@app
def hello():
    return 'hello welcome to flask'
