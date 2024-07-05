from flask import *
#We name our flask
app=Flask(__name__)
#we route then create function that returns a value hello
@app.route('/hello')
def hello():
    return 'hello'
@app.route(/goods)







#displaying or running the code we do the following
#If the code/script runs here in the main virtual window we are using,
#it should run and debug
if (__name__)==('__main__'):
    app.run(debug=True)