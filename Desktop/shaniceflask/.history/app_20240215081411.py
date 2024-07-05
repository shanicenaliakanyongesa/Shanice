from flask import *
app=Flask(__name__)
@app.route('/hello')
def hello():
    return 'hello'
if (__name__)==('__main__'):
    app