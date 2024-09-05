from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, validators, SelectField

class ViloyatForm(FlaskForm):
    respublika = SelectField(label="Select Respublika", validators=[validators.DataRequired("Required")])
    text = StringField(label="Enter Viloyat Name", validators=[validators.DataRequired("Required")])
    submit = SubmitField(label="Submit")
