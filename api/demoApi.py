import requests

class Direccion(object):
	direccion = ""
	colonia = ""
	ciudad = ""
	pais = ""

	def __init__(self):
		self.endpoint = "https://maps.googleapis.com/maps/api/geocode/json"
		self.apikey = "AIzaSyBbXf1XV-hukV_3BPmyGxm8WjEqDahTnFI"
		

	def obtenDireccion(self, latitud, longitud):
		parameters = {"latlng":latitud + ", " + longitud, "key":self.apikey}
		resultado = requests.get(self.endpoint, params=parameters).json()
		print(resultado)
		listado = resultado["results"][0]
		self.direccion = listado["formatted_address"]
		self.colonia = listado["address_components"][2]["long_name"]
		self.ciudad = listado["address_components"][3]["long_name"]
		self.pais = listado["address_components"][6]["long_name"]
		return self

