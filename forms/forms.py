from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired

class Formulario(Form):
	latitud = StringField('Latitud', validators=[DataRequired()])
	longitud = StringField('Longitud', validators=[DataRequired()])