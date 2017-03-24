#Windows
# $ set FLASK_DEBUG=1	                        #enable debug 
# $ set FLASK_APP=ex2-hellow_without_app_run.py
# $ flask run

#Unix

# $ export FLASK_APP=ex2-hellow_without_app_run.py
# $　flask run


#result  no debug 

# * Serving Flask app "ex2-hellow_without_app_run"
# * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)


#result  debug = 1
#* Serving Flask app "ex2-hellow_without_app_run"
# * Forcing debug mode on
# * Restarting with stat
# * Debugger is active!
# * Debugger PIN: 322-270-699
# * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
# 127.0.0.1 - - [24/Mar/2017 13:38:17] "GET / HTTP/1.1" 200 -
# * Detected change in 'F:\\Google Drive\\碩士論文\\flask\\example\\ex2-hellow_without_app_run\\ex2-hellow_without_app_run.py', reloading

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!!!  Debug!!!'
	
