from flask import Flask, render_template

app = Flask(__name__)

@app.route('/main',methods=['GET'])
def index():
    return render_template("index.html")
@app.route('/request')
def request():
    return 'OK'