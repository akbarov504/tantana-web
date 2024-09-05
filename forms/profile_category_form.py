from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, validators

class ProfileCategoryForm(FlaskForm):
    title = StringField(label="Enter Profile Category Title", validators=[validators.DataRequired("Required")])
    description = StringField(label="Enter Profile Category Description", validators=[validators.DataRequired("Required")])
    submit = SubmitField(label="Submit")
