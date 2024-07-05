#importing modules/tools necessary for our flask to function
from flask import *
#giving our app.py a na
app=Flask(__name__)

@app.route('/hello')
def hello():
    return 'hello welcome to flask'

