from flask import *
app=Flask(__name__)
@app.route('/hello')
def hello():
    return 'hello'

@app.route('/home')
def home():
    return render_template('home.html')

if (__name__) == ('__main__'):
    app.run(debug=True)