from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, validators

class RespublikaForm(FlaskForm):
    text = StringField(label="Enter Respublika Name", validators=[validators.DataRequired("Required")])
    submit = SubmitField(label="Submit")
