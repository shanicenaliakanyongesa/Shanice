from flask import *
app=Flask(__name__)

@app.route('')
def hello():
    return 'hello welcome to flask'
