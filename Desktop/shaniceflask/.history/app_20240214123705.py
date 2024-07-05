#first thing is to import modules/tools needed from flask
from flask import *
app=Flask(__name__)

#homepage route/location
@app.route('/homepage')
def homepage():
    return 'welcome to homepage'
#route/location for hello
@app.route('/hello')
def hello():
    return 'hello good morning '

#route/ for help
@app.route('/help')
def help():
    return 'help'

#linking/routing our html file
@app.route('/tumaini')
def tumaini():
    return render_template('tumaini.html')

#routing 


#display or run our file to get output

if (__name__)==('__main__'):
    app.run(debug=True)



