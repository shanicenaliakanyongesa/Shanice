#importing modules/tools necessary for our flask to function
from flask import *
#giving our app.py a name, this is the default way of doing so.
app=Flask(__name__)
#here we are routing, we always route before our function
@app.route('/hello')
#we now write the function
def hello():
    return 'hello welcome to flask'
if(__name__)==('')

