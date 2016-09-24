import requests

class Direccion(object):
	direccion = ""
	ciudad = ""
	pais = ""
	apikey = "AIzaSyBbXf1XV-hukV_3BPmyGxm8WjEqDahTnFI"
	endpoint = "https://maps.googleapis.com/maps/api/geocode/json"

	def __init__(self):
		return

	def obtenDireccion(self, *args):
		print(args)
		try:
			parameters = {"latlng":args[0] + ", " + args[1], "key":self.apikey}
			resultado = requests.get(self.endpoint, params=parameters).json()
			# print(resultado)
			listado = resultado["results"][0]
			self.direccion = listado["formatted_address"]
			self.ciudad = listado["address_components"][3]["long_name"]
			self.pais = listado["address_components"][6]["long_name"]
			return self
		except:
			print("Tuvimos un erro en la api")
			return False