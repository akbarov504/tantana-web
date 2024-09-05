from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField, validators
from flask_wtf.file import FileField

class ProfileImageForm(FlaskForm):
    image = FileField(label="Enter Profile Image", validators=[validators.DataRequired("Required")])
    profile = SelectField(label="Select Profile", validators=[validators.DataRequired("Required")])
    submit = SubmitField(label="Submit")
