from flask import *
app=Flask(__name__)
@app.route('/hello')
def hello():
    retun 'hello sokogarden'