'''importo desde la carpeta de mi aplicacion
el archivo app.py que contiene la configuracion
de mi archivo'''
from app import app
from flask import render_template
from miApi.api import Direccion 

@app.route("/")
def index():
	contexto = ["Xime", "Elena", "Mariana"]
	return render_template("index.html", data=contexto)

@app.route("/api")
def api():
	miDireccion = Direccion()
	resultado = miDireccion.obtenDireccion("19.4302247", "-99.2110075")
	if resultado != False:
		return render_template("direccion.html", data=resultado)
	else:
		return render_template("404.html")
