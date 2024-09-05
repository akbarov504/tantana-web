from app import root
from models import models
from forms.user_form import RegisterForm, LoginForm
from flask import render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required

@root.route("/register", methods=["GET", "POST"])
def register_page() -> render_template:
    form = RegisterForm()
    if form.validate_on_submit():
        full_name = form.full_name.data
        phone = form.phone.data
        password = form.password.data
        user = models.User.query.filter_by(phone=phone, password=password, is_deleted=False).first()
        if user is None:
            user = models.User(full_name, phone, password, 'UZ', 'USER', -1)
            models.db.session.add(user)
            models.db.session.commit()
            flash("Successfully registered!", category="success")
            return redirect(url_for("home_page"))
        else:
            flash("This user is already register!", category="danger")
            return redirect(url_for("register_page"))
    else:
        return render_template("register.html", form=form)

@root.route("/login", methods=["GET", "POST"])
def login_page() -> render_template:
    form = LoginForm()
    if form.validate_on_submit():
        phone = form.phone.data
        password = form.password.data
        user = models.User.query.filter_by(phone=phone, password=password, is_deleted=False).first()
        if user is None:
            flash("Username or Password are not match! Please try again!", category="danger")
            return render_template("login.html", form=form)
        else:
            login_user(user)
            if user.role == "USER":
                flash("Succesfully loged in!", category="success")
                return redirect(url_for("home_page"))
            elif user.role == "ADMIN":
                flash("Succesfully loged in!", category="success")
                return redirect(url_for("admin_page"))
            else:
                flash("Succesfully loged in!", category="success")
                return redirect(url_for("home_page"))
    else:
        return render_template("login.html", form=form)

@root.route("/logout", methods=["GET", "POST"])
@login_required
def logout_page():
    logout_user()
    return redirect(url_for("home_page"))
