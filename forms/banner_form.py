from flask_wtf import FlaskForm
from wtforms import SubmitField, URLField, validators
from flask_wtf.file import FileField

class BannerForm(FlaskForm):
    image = FileField(label="Enter Banner Image", validators=[validators.DataRequired("Required")])
    url = URLField(label="Enter Banner URL", validators=[validators.DataRequired("Required")])
    submit = SubmitField(label="Submit")
