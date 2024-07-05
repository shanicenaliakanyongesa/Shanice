
from sqlite3 import Cursor
from flask import *
import pymysql 
connection=pymysql.connect(  host='localhost', user='root',password='', database='sokogarden'
 )
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
    
    
@app.route('/single/<product_id')
def single(product_id):
    sql1= "select * from products where product_id=%s"
    
    Cursor.execute(sql1,product_id)
    product = Cursor.fetchone()
    return render_template('single_item.html', product=product)

    

   
   
   
@app.route('/upload', methods=['POST', 'GET']) 
def upload():
    if request.method=='POST':
        product_name=request.form['product_name']
        product_desc=request.form['product_desc']
        product_cost=request.form['product_cost']
        product_category=request.form['product_category']
        product_image_name=request.files['product_image_name']
        product_image_name.save('static/images/'+ product_image_name.filename)
        #connecting our sql database
        connection=pymysql.connect(
            host='localhost', user='root', password='', database='sokogarden'
        )
        cursor=connection.cursor()
        data=(product_name,product_desc,product_cost,product_category,product_image_name.filename)
        sql="insert into products (product_name,product_desc,product_cost,product_category,product_image_name) values(%s,%s,%s,%s,%s)"
        try:
            cursor.execute(sql,data)
            connection.commit()
            return render_template('upload.html', message='Products Added Successfully')
        except:
            connection.rollback()
            return render_template('upload.html' , message='Failed Try Again')
    else:
        return render_template('upload.html', message='Please Add Product Details')    
            















if (__name__) == ('__main__'):
   app.run(debug=True)
    
   
   


 