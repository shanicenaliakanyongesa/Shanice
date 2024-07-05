from flask import *
#We name our flask
app=Flask(__name__)
@app.route('/hello')
def hello():