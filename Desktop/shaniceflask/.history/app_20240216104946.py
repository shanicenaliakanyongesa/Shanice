from flask import *
import pymysql
app=Flask(__name__)
@app.route('/hello')
def hello():
    return 'hello sokogarden'
@app.route('/home')
def home():
    return render_template('home.html')
@app.route('/upload', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':#IF WE ARE SUBMITTING THE FORM, THEN SOMETHING SHOULD BE DONE  
         product_name=request.form['product_name']
         product_desc=request.form['product_desc']
         product_cost=request.form['product_cost']
         product_category=request.form['product_category']
         product_image_name=request.file['product_image_name']
         product_image_name.save('static/images/'+ product_image_name.filename)#saves the image to static folder inside images folder
#connecting to our database with our upload.html

         connection=pymysql.connect(
            host='localhost', user='root',password='', database='sokogarden'  
         )
         #facilitates sql queries
         cursor=connection.cursor()
         data=(product_name,product_desc,product_cost,product_category,product_image_name.filename)
         sql="insert into products(product_name,product_desc,product_cost,product_category,product_image_name values %s, %s, %s, %s, %s)"
          
    try:#here we are executing sql/ parsing data
        cursor.execute(sql,data)
        connection.commit()
        return render_template('upload.html', message='Product Added Successfully')
    except:
        connection.rollback()
        return render_template('upload.html', message='Failed Try Again Later')
    else:
        ret
   
   
   
   
        
   
   
   
   
   
   

 






if (__name__) == ('__main__'):
    app.run(debug=True)