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
        sql="insert into products (product_name,product_desc,product_cost,product_category,product_image_name)"
        try:
            cursor.execute(sql,data)
            connection.commit()
            return render_template('upload.html', message='Products Added Successfully')
        except:
            connection.rollback()
            
            















if (__name__) == ('__main__'):
   app.run(debug=True)
    
   
   


 