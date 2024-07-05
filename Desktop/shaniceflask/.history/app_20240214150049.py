from flask import *
#We name our flask
app=Flask(__name__)
#we route then creat 
@app.route('/hello')
def hello():
    return 'hello'