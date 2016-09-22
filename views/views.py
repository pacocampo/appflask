'''importo desde la carpeta de mi aplicacion
el archivo app.py que contiene la configuracion
de mi archivo'''
from app import app
from flask import render_template

@app.route("/")
def index():
	contexto = ["Xime", "Elena", "Mariana"]
	return render_template("index.html", data=contexto)