#immporting modules/tools necessary for our flask 
from flask import *

app=Flask(__name__)

@app.route('/hello')
def hello():
    return 'hello welcome to flask'

