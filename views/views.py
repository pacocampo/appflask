'''importo desde la carpeta de mi aplicacion
el archivo app.py que contiene la configuracion
de mi archivo'''
from app import app
from flask import render_template
from miApi.api import Direccion
from forms.forms import Formulario, ProductoForm
import json
#importamos la libreria de firebase
import pyrebase

#Creamos una funcion que regrese un objeto firebase ya con las credenciales
def firebaseObject():
	# Llena con los datos de tu app de firebase
	config = {
	"apiKey": "",
	"authDomain": "",
	"databaseURL": "",
	"storageBucket": ""
	}
	# Inicializa un objeto firebase
	firebase = pyrebase.initialize_app(config)

	return firebase

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
	# Creamos un objeto firebase (funcion de arriba)
	fbase = firebaseObject()
	# Creamos un objeto Firebase Authentication para validar al usuario registrado
	auth = fbase.auth()
	# Obtenemos los datos del usuario (no necesario para futuras transacciones)
	user = auth.sign_in_with_email_and_password('paco.ocampor@gmail.com', '41000705')
	# Creamos un objeto Firebase database
	db = fbase.database()
	# Obtenemos los registro de producto ("/producto")
	result = db.child("producto").get()
	# Formularios
	formulario = ProductoForm()
	if formulario.validate_on_submit():
		# Creamos un diccionario con los datos que vamos a guardar dentro de firebase
		data = {"nombre":formulario.nombre.data, "precio" : formulario.precio.data, "categoria" :{"categoria": 3}}
		# Hacemos el registro dentro de producto con la funcion "push" que recibe nuestro diccionario
		db.child("producto").push(data)
	return render_template("producto.html", data=result.val(), form=formulario)

@app.route("/producto/<id>")
def detailProduct(id=None):
	# Creamos un objeto firebase (funcion de arriba)
	fbase = firebaseObject()
	# Creamos un objeto Firebase database
	db = fbase.database()
	# Obtenemos el detalle del producto, en el primer child establecemos
	# el parent de la informacion que queremos detallar en este caso "producto"
	# en el segundo child pasamos el id del producto
	products = db.child("producto").child(id).get()
	#regresamos el resultado del products con la funcion each que lo convierte en un objeto iterable
	return render_template("detail.html", producto=products.each())
