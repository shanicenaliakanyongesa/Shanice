from flask import *
app=Flask(__name__)
@app.route('/hello')
def hello():
    return 'hello sokogarden'
@app.route('/home')
def home():
    return render

if (__name__) == ('__main__'):
    app.run(debug=True)