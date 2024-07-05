from flask import *

app=Flask(__name__)

@app.route('/hello')
def hello():
    return 'hello welcome to flask'

