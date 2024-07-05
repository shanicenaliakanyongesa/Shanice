from flask import *
app=Flask(__name__)
@app.route('/hello')
def hello():
    return 'hello sokogarden'
@app.route('/home')
def home():
    return render_template('home.html')
@app.route('/upload', methods=['POST', 'GET'])
def upload():
    return render_template('upload.html')
#we are posting/uploading our products and then connect our database
if request.method == 'POST':#IF WE ARE SUBMITTING THE FORM, THEN SOMETHING SHOULD BE DONE
    product_name=request.form['product_name']
    product_desc=request.form['product_desc']
    product_cost=request.form['product_cost']
    product_category=request.form['product_category']
    product_image_name=request.file['product_image_name']
    product_image_name.save('static/images/'+ product_image_name.filename)#saves the image to static folder inside images folder
#connecting to our database with our upload.html
import pymysql
connection=pymysql.connect
cursor=connection.cursor
data=(product_name,product_desc,product_cost,product_category,product_image_name.filename)
sql="insert into "







if (__name__) == ('__main__'):
    app.run(debug=True)