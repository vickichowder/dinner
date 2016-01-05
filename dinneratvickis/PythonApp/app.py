from flask import Flask, render_template, json, request, redirect
from datetime import datetime
from flask.ext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL()

# MySQL config
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ' '
app.config['MYSQL_DATABASE_DB'] = 'dinneratvickis'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

@app.route("/")
def main():
	return render_template('index.html')

@app.route("/comingUp")
def comingUp():
	return render_template('comingUp.html')

@app.route("/showWeAte")
def showWeAte():
	return render_template('weAte.html')

@app.route("/weAte", methods=['GET'])
def weAte():
	# fetching from form
	guests = request.form['names']
	donation = request.form['amount']
	if (guests!="") and (donation!=""):
		return render_template('index.html')
	else:
		return render_template('index.html') 
		
if __name__ == "__main__":
	app.run(port=8000)