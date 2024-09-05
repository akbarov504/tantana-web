from flask_wtf import FlaskForm
from wtforms import SubmitField, URLField, validators
from flask_wtf.file import FileField

class SliderForm(FlaskForm):
    image = FileField(label="Enter Slider Image", validators=[validators.DataRequired("Required")])
    url = URLField(label="Enter Slider URL", validators=[validators.DataRequired("Required")])
    submit = SubmitField(label="Submit")
