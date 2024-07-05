#first thing is to import modules/tools needed from flask
from flask import *
app=(__name__)
@app.route('/ homepage')
def homepage():
    return 'welcome to hom'

