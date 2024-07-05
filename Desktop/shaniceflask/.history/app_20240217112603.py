
from sqlite3 import Cursor
from flask import *
import pymysql 
connection=pymysql.connect(  host='localhost', user='root',password='', database='sokogarden')

cursor= connection.cursor()

app=Flask(__name__)

@app.route('/hello')
def hello():
    return 'hello sokogarden'

@app.route('/about')
def about():
    return 'sokogarden'

@app.route('/')
def home():
    # SQL 1  - Smartphones
    sql1 = "SELECT * FROM products where product_category = 'x'"
    # Cursor - Used to run/execute above SQL
    cursor = connection.cursor()
    # Execute SQL
    cursor.execute(sql1)
    # Fetch Rows
    smartphones = cursor.fetchall()

    # SQL 2  - Detergents
    sql2 = "SELECT * FROM products where product_category = 'y'"

    # Execute SQL
    cursor.execute(sql2)
    # Fetch Rows
    detergents = cursor.fetchall()

    return render_template('home.html', detergents=detergents,
                           smartphones=smartphones)

    
    
@app.route('/single_item/<product_id>')
def single(product_id):
    sql1= "select * from products where product_id=%s"
    
    cursor.execute(sql1,product_id)
    product = cursor.fetchone()
    return render_template('single_item.html', product=product)

@app.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
            username = request.form['username']
            email = request.form['email']
            phone = request.form['phone']
            password1 = request.form['password1']
            password2 = request.form['password2']

            if len(password1) < 8:
                return render_template('signup.html', error='Password must more than 8 xters')
            elif password1 != password2:
                return render_template('signup.html', error='Password Do Not Match')
            else: 
                sql = ''' 
                     insert into users(username, password, email,phone) 
                     values(%s, %s, %s, %s)
                 '''
                cursor = connection.cursor()
                cursor.execute(sql, (username, password1, email, phone,))
                connection.commit()
                return render_template('signup.html', success='Registered Successfully')

    else:
        return render_template('signup.html')

    

   
   
   
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
    
   
   


 