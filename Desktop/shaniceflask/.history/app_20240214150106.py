from flask import *
#We name our flask
app=Flask(__name__)
#we route then create function that returns a value hello
@app.route('/hello')
def hello():
    return 'hello'