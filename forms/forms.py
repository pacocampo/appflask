from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired

class Formulario(Form):
	latitud = StringField('Latitud', validators=[DataRequired()])
	longitud = StringField('Longitud', validators=[DataRequired()])

class ProductoForm(Form):
	nombre = StringField('Nombre de producto', validators=[DataRequired()])
	precio = StringField('Precio', validators=[DataRequired()])