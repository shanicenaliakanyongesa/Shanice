from flask import *
import pymysql 
app=Flask(__name__)
@app.route('/hello')
def hello():
    return 'hello sokogarden'
@app.route('/about')
def about():
    return 'sokogarden'

@app.route('/home')
def home():
     return render_template ('home.html')
@app.route('/upload', methods=['POST','GET'])
def upload():
    if request.method=='POST':
        product_name=requst.form['']
     
 
if (__name__) == ('__main__'):
   app.run(debug=True)
   


 