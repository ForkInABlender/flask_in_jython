from flask import Flask, request

from java.lang import System

app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        #print(request.data)
        System.out.println("%s" % request.data)
    return "it worked"

app.run(host="127.0.0.1", port=5000)
