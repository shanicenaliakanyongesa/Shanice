from flask import *
app=Flask(__name__)
@app.route('/hello')
def hello():
    return 'hello sokogarden'
if (__name__)==('__main__'):
pp.run(debug=True)