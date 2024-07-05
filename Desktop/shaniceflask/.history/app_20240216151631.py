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
@app.route('/upload')
def upload():
if (__name__)  ('')  
   
   


 