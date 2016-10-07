'''importo desde la carpeta de mi aplicacion
el archivo app.py que contiene la configuracion
de mi archivo'''
from app import app
from flask import render_template
from miApi.api import Direccion
from forms.forms import Formulario, ProductoForm
import json
from firebase import firebase

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

@app.route("/producto", methods=('GET', 'POST'))
def producto():
	formulario = ProductoForm()
	fbase = firebase.FirebaseApplication('https://demoflask-99c26.firebaseio.com/', None)
	if formulario.validate_on_submit():
		fbase.post('/producto/categoria', {"categoria":formulario.nombre.data, "tag":formulario.precio.data})
	result = fbase.get('/producto/categoria', None)
	print(result)

	return render_template("producto.html", data = result, form=formulario)

@app.route("/producto/<id>")
def detailProduct(id=None):
	print id
	fbase = firebase.FirebaseApplication('https://demoflask-99c26.firebaseio.com/', None)

	products = fbase.get('/producto/categoria', None)

	product = products[id]
	return render_template("detail.html", producto=product)



















