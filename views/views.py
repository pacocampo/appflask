'''importo desde la carpeta de mi aplicacion
el archivo app.py que contiene la configuracion
de mi archivo'''
from app import app
from flask import render_template
from miApi.api import Direccion
from forms.forms import Formulario

@app.route("/")
def index():
	contexto = ["Xime", "Elena", "Mariana"]
	return render_template("index.html", data=contexto)

@app.route("/api", methods=('GET', 'POST'))
def api():
	miForm = Formulario()
	if miForm.validate_on_submit():
		miDireccion = Direccion()
		resultado = miDireccion.obtenDireccion(miForm.latitud.data, miForm.longitud.data)
		if resultado != False:
			return render_template("direccion.html", data=resultado, form=miForm)
		else:
			return render_template("404.html")
	else:
		return render_template("direccion.html", data=Direccion(), form=miForm)
