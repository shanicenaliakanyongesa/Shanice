from flask import *
app=Flask(__name__)
@app.route('/hello')
def hello():
    return 'hello sokogarden'
@app.route('/home')
def home():
    return render_template('home.html')
@app.route('/upload')
def upload():
    return render_template('upload.html')
#we are posting/uploading our products and then connect our database
if request.method ===


if (__name__) == ('__main__'):
    app.run(debug=True)