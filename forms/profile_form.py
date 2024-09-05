from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, SelectField, validators
from flask_wtf.file import FileField, MultipleFileField

class ProfileForm(FlaskForm):
    title = StringField(label="Enter Profile Title", validators=[validators.DataRequired("Required")])
    description = StringField(label="Enter Profile Description", validators=[validators.DataRequired("Required")])
    image = FileField(label="Enter Profile Image", validators=[validators.DataRequired("Required")])
    category = SelectField(label="Select Profile Category", validators=[validators.DataRequired("Required")])
    images = MultipleFileField(label="Select Profile Multiple Images", validators=[validators.DataRequired("Required")])
    respublika = SelectField(label="Select Profile Respublika", validators=[validators.DataRequired("Required")])
    viloyat = SelectField(label="Select Profile Viloyat", validators=[validators.DataRequired("Required")])
    tuman = SelectField(label="Select Profile Tuman", validators=[validators.DataRequired("Required")])
    submit = SubmitField(label="Submit")
