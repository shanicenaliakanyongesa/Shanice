#first thing is to import modules/tools needed from flask
from flask import *
app=(__name__)

#homepage 
@app.route('/ homepage')
def homepage():
    return 'welcome to homepage'



