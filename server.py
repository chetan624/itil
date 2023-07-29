from flask import Flask

app = Flask(__name__)

@app.route("/",methods=["GET"])
def root():
     return "Welcome to python application..."

app.run(host="0.0.0.0", port=4000, debug=True)

from flask import Flask

app = Flask(__name__)

@app.route("/",methods=["GET"])
def root():
     return "devops"

app.run(host="0.0.0.0", port=4000, debug=True)

from flask import Flask

app = Flask(__name__)

@app.route("/",methods=["GET"])
def root():
     return "PRN,NAME, Phone Number"

app.run(host="0.0.0.0", port=4000, debug=True)

