#first thing is to import modules/tools needed from flask
from flask import *
app=(__name__)

#homepage route/location
@app.route()'/homepage')
def homepage():
    return 'welcome to homepage'

#display or run our file to get output

if (__name__)==('__main__'):
    app.run(debug=True)



