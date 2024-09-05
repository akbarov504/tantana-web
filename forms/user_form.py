from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField, validators

class LoginForm(FlaskForm):
    phone = StringField(label="Enter Your Phone Number", validators=[validators.Length(min=13, max=13), validators.DataRequired("Required"), validators.Regexp("^\+998(50|99|97|98|95|20|93|94|33|55|61|62|65|66|67|69|70|71|72|73|74|75|76|77|78|79|88|90|91)(\d{7})$")])
    password = PasswordField(label="Enter Your Password", validators=[validators.Length(min=8, max=300), validators.DataRequired("Required")])
    submit = SubmitField(label="Login")

class RegisterForm(FlaskForm):
    full_name = StringField(label="Enter Your Full name")
    phone = StringField(label="  Enter Your Phone", validators=[validators.Length(min=13, max=13), validators.DataRequired("Required"), validators.Regexp("^\+998(50|99|97|98|95|20|93|94|33|55|61|62|65|66|67|69|70|71|72|73|74|75|76|77|78|79|88|90|91)(\d{7})$")])
    password = PasswordField(label="Enter Your Password", validators=[validators.Length(min=8, max=300), validators.DataRequired("Required")])
    submit = SubmitField(label="Register")
