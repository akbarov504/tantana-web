from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, validators

class MessageForm(FlaskForm):
    message = StringField(label="Enter message", validators=[validators.DataRequired("Required")])
    submit = SubmitField(label="Submit", validators=[validators.DataRequired("Required")])
