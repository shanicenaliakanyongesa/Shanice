from flask import *
#We name our flask
app=Flask(__name__)
#we route 
@app.route('/hello')
def hello():
    return 'hello'