from flask import Flask, render_template, jsonify,url_for,redirect
import json
import random
app = Flask(__name__)

#important pages:
#http://stackoverflow.com/questions/24719592/sending-data-as-json-object-from-python-to-javascript-with-jinja
#http://stackoverflow.com/questions/15801782/how-to-correctly-pass-a-json-object-to-flask-server-using-jquery-ajax

#interesting example to try later: https://realpython.com/blog/python/web-development-with-flask-fetching-data-with-requests/
@app.route("/",methods=["GET","POST"])
def index():
    #data = {"data":[1,2,3,4,5,6,7,8]}
    data = [random.randint(0,1000) for elem in xrange(200)]
    return render_template("index.html",data=json.dumps(data))

app.run(debug=True)
