#importing modules/tools necessary for our flask to function
from flask import *
#giving our app.py a name, this is the default way of doing so.
app=Flask(__name__)
#here we are routing, we always route before our function
@app.route('/hell')
#we now write the function
def hell():
    return 'hello welcome to flask'
@app.route('/about_us')
def about_us():
    return 'about us'
@app.route('/news')
def news():
    return 'todays news'
@app.p

#this code below means that if the app/code is running in this main window we run then debug if an error occurs
if(__name__)==('__main__'):
    app.run(debug=True)

