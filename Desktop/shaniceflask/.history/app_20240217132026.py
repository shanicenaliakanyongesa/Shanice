
import sms
from flask import *
import pymysql 
import requests
import datetime
import base64
from requests.auth import HTTPBasicAuth
connection=pymysql.connect(  host='localhost', user='root',password='', database='sokogarden')

cursor= connection.cursor()

app=Flask(__name__)
print(__name__)
# set secret key to secure your session/make it unique
app.secret_key = "AW_r%@jN*HU4AW_r%@jN*HU4AW_r%@jN*HU4"
# Decorate your app with features
# http://127.0.0.1:5000/home


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
                sms.send_sms(phone, 'thank you for registering')
                return render_template('signup.html', success='Registered Successfully')

    else:
        return render_template('signup.html')
@app.route('/signin', methods=['POST', 'GET'])
def signin():
    
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']      

        sql = '''
           select * from users where username = %s and password = %s
        '''
        cursor = connection.cursor()
        cursor.execute(sql, (username, password))

        if cursor.rowcount == 0:
            return render_template('signin.html', error='Invalid Credentials')
        else:
            session['key'] = username  # link the session key with username
            return redirect('/')  # redirect to product Default route
    else:
        return render_template('signin.html')
    

    
@app.route('/logout')   
def logout():
    session.clear()
    return render_template('/signin.html')
#or return redirect('/login')
   
   
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
@app.route('/mpesa', methods=['POST', 'GET'])
def mpesa_payment():
    if request.method == 'POST':
        phone = str(request.form['phone'])
        amount = str(request.form['amount'])
        # GENERATING THE ACCESS TOKEN
        # create an account on safaricom daraja
        consumer_key = "GTWADFxIpUfDoNikNGqq1C3023evM6UH"
        consumer_secret = "amFbAoUByPV2rM5A"

        api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"  # AUTH URL
        r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))

        data = r.json()
        access_token = "Bearer" + ' ' + data['access_token']

        #  GETTING THE PASSWORD
        timestamp = datetime.datetime.today().strftime('%Y%m%d%H%M%S')
        passkey = 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919'
        business_short_code = "174379"
        data = business_short_code + passkey + timestamp
        encoded = base64.b64encode(data.encode())
        password = encoded.decode('utf-8')

        # BODY OR PAYLOAD
        payload = {
            "BusinessShortCode": "174379",
            "Password": "{}".format(password),
            "Timestamp": "{}".format(timestamp),
            "TransactionType": "CustomerPayBillOnline",
            "Amount": "1",  # use 1 when testing
            "PartyA": phone,  # change to your number
            "PartyB": "174379",
            "PhoneNumber": phone,
            "CallBackURL": "https://modcom.co.ke/job/confirmation.php",
            "AccountReference": "account",
            "TransactionDesc": "account"
        }

        # POPULAING THE HTTP HEADER
        headers = {
            "Authorization": access_token,
            "Content-Type": "application/json"
        }

        url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"  # C2B URL

        response = requests.post(url, json=payload, headers=headers)
        print(response.text)
        return '<h3>Please Complete Payment in Your Phone and we will deliver in minutes</h3>' \
               '<a href='' class="btn btn-dark btn-sm">Back to Products</a>'
@app.route('/mpesa', methods=['POST', 'GET'])
def mpesa_payment():
    if request.method == 'POST':
        phone = str(request.form['phone'])
        amount = str(request.form['amount'])
        # GENERATING THE ACCESS TOKEN
        # create an account on safaricom daraja
        consumer_key = "GTWADFxIpUfDoNikNGqq1C3023evM6UH"
        consumer_secret = "amFbAoUByPV2rM5A"

        api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"  # AUTH URL
        r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))

        data = r.json()
        access_token = "Bearer" + ' ' + data['access_token']

        #  GETTING THE PASSWORD
        timestamp = datetime.datetime.today().strftime('%Y%m%d%H%M%S')
        passkey = 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919'
        business_short_code = "174379"
        data = business_short_code + passkey + timestamp
        encoded = base64.b64encode(data.encode())
        password = encoded.decode('utf-8')

        # BODY OR PAYLOAD
        payload = {
            "BusinessShortCode": "174379",
            "Password": "{}".format(password),
            "Timestamp": "{}".format(timestamp),
            "TransactionType": "CustomerPayBillOnline",
            "Amount": "1",  # use 1 when testing
            "PartyA": phone,  # change to your number
            "PartyB": "174379",
            "PhoneNumber": phone,
            "CallBackURL": "https://modcom.co.ke/job/confirmation.php",
            "AccountReference": "account",
            "TransactionDesc": "account"
        }

        # POPULAING THE HTTP HEADER
        headers = {
            "Authorization": access_token,
            "Content-Type": "application/json"
        }

        url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"  # C2B URL

        response = requests.post(url, json=payload, headers=headers)
        print(response.text)
        return '<h3>Please Complete Payment in Your Phone and we will deliver in minutes</h3>' \
               '<a href='' class="btn btn-dark btn-sm">Back to Products</a>'














if (__name__) == ('__main__'):
   app.run(debug=True)
    
   
   


 