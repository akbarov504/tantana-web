import os
from app import root
from models import models
from forms.profile_category_form import ProfileCategoryForm
from forms.respublika_form import RespublikaForm
from forms.viloyat_form import ViloyatForm
from forms.tuman_form import TumanForm
from forms.banner_form import BannerForm
from forms.slider_form import SliderForm
from werkzeug.utils import secure_filename
from flask import render_template, url_for, redirect
from flask_login import login_required, current_user

@root.route("/admin", methods=["GET", "POST"])
@login_required
def admin_page() -> render_template:
    if current_user.role == "ADMIN":
        respublika_l = models.Respublika.query.filter_by(is_deleted=False).all()
        viloyat_l = models.Viloyat.query.filter_by(is_deleted=False).all()
        tuman_l = models.Tuman.query.filter_by(is_deleted=False).all()
        category_l = models.ProfileCategory.query.filter_by(is_deleted=False).all()
        return render_template("admin.html", category_list=category_l, respublika_list=respublika_l, viloyat_list=viloyat_l, tuman_list=tuman_l)
    else:
        return redirect(url_for("home_page"))

# category
@root.route("/admin/category/list", methods=["GET", "POST"])
@login_required
def admin_category_list_page() -> render_template:
    if current_user.role == "ADMIN":
        respublika_l = models.Respublika.query.filter_by(is_deleted=False).all()
        viloyat_l = models.Viloyat.query.filter_by(is_deleted=False).all()
        tuman_l = models.Tuman.query.filter_by(is_deleted=False).all()
        category_l = models.ProfileCategory.query.filter_by(is_deleted=False).all()
        return render_template("admin-category-list.html", category_list=category_l, respublika_list=respublika_l, viloyat_list=viloyat_l, tuman_list=tuman_l)
    else:
        return redirect(url_for("home_page"))

@root.route("/admin/category/update/<id>", methods=["GET", "POST"])
@login_required
def admin_category_update_page(id) -> render_template:
    if current_user.role == "ADMIN":
        form = ProfileCategoryForm()
        if form.validate_on_submit():
            category = models.ProfileCategory.query.filter_by(id=id, is_deleted=False).first()
            title = form.title.data
            description = form.description.data
            category.title = title
            category.description = description
            models.db.session.commit()
            return redirect(url_for("admin_category_list_page"))
        else:
            category = models.ProfileCategory.query.filter_by(id=id, is_deleted=False).first()
            form.title.data = category.title
            form.description.data = category.description
            respublika_l = models.Respublika.query.filter_by(is_deleted=False).all()
            viloyat_l = models.Viloyat.query.filter_by(is_deleted=False).all()
            tuman_l = models.Tuman.query.filter_by(is_deleted=False).all()
            return render_template("admin-category-update.html", form=form, respublika_list=respublika_l, viloyat_list=viloyat_l, tuman_list=tuman_l)
    else:
        return redirect(url_for("home_page"))

@root.route("/admin/category/delete/<id>", methods=["GET", "POST"])
@login_required
def admin_category_delete_page(id) -> render_template:
    if current_user.role == "ADMIN":
        category = models.ProfileCategory.query.filter_by(id=id, is_deleted=False).first()
        category.is_deleted = True
        models.db.session.commit()
        return redirect(url_for("admin_category_list_page"))
    else:
        return redirect(url_for("home_page"))

@root.route("/admin/category/create", methods=["GET", "POST"])
@login_required
def admin_category_create_page() -> render_template:
    if current_user.role == "ADMIN":
        form = ProfileCategoryForm()
        if form.validate_on_submit():
            title = form.title.data
            description = form.description.data
            category = models.ProfileCategory(title, description, current_user.id)
            models.db.session.add(category)
            models.db.session.commit()
            return redirect(url_for("admin_category_list_page"))
        else:
            respublika_l = models.Respublika.query.filter_by(is_deleted=False).all()
            viloyat_l = models.Viloyat.query.filter_by(is_deleted=False).all()
            tuman_l = models.Tuman.query.filter_by(is_deleted=False).all()
            return render_template("admin-category-create.html", form=form, respublika_list=respublika_l, viloyat_list=viloyat_l, tuman_list=tuman_l)
    else:
        return redirect(url_for("home_page"))

# respublika
@root.route("/admin/respublika/list", methods=["GET", "POST"])
@login_required
def admin_respublika_list_page() -> render_template:
    if current_user.role == "ADMIN":
        respublika_l = models.Respublika.query.filter_by(is_deleted=False).all()
        viloyat_l = models.Viloyat.query.filter_by(is_deleted=False).all()
        tuman_l = models.Tuman.query.filter_by(is_deleted=False).all()
        return render_template("admin-respublika-list.html", respublika_list=respublika_l, viloyat_list=viloyat_l, tuman_list=tuman_l)
    else:
        return redirect(url_for("home_page"))

@root.route("/admin/respublika/update/<id>", methods=["GET", "POST"])
@login_required
def admin_respublika_update_page(id) -> render_template:
    if current_user.role == "ADMIN":
        form = RespublikaForm()
        if form.validate_on_submit():
            respublika = models.Respublika.query.filter_by(id=id, is_deleted=False).first()
            text = form.text.data
            respublika.text = text
            models.db.session.commit()
            return redirect(url_for("admin_respublika_list_page"))
        else:
            respublika = models.Respublika.query.filter_by(id=id, is_deleted=False).first()
            form.text.data = respublika.text
            respublika_l = models.Respublika.query.filter_by(is_deleted=False).all()
            viloyat_l = models.Viloyat.query.filter_by(is_deleted=False).all()
            tuman_l = models.Tuman.query.filter_by(is_deleted=False).all()
            return render_template("admin-respublika-update.html", form=form, respublika_list=respublika_l, viloyat_list=viloyat_l, tuman_list=tuman_l)
    else:
        return redirect(url_for("home_page"))

@root.route("/admin/respublika/delete/<id>", methods=["GET", "POST"])
@login_required
def admin_respublika_delete_page(id) -> render_template:
    if current_user.role == "ADMIN":
        respublika = models.Respublika.query.filter_by(id=id, is_deleted=False).first()
        respublika.is_deleted = True
        models.db.session.commit()
        return redirect(url_for("admin_respublika_list_page"))
    else:
        return redirect(url_for("home_page"))

@root.route("/admin/respublika/create", methods=["GET", "POST"])
@login_required
def admin_respublika_create_page() -> render_template:
    if current_user.role == "ADMIN":
        form = RespublikaForm()
        if form.validate_on_submit():
            text = form.text.data
            respublika = models.Respublika(text, current_user.id)
            models.db.session.add(respublika)
            models.db.session.commit()
            return redirect(url_for("admin_respublika_list_page"))
        else:
            respublika_l = models.Respublika.query.filter_by(is_deleted=False).all()
            viloyat_l = models.Viloyat.query.filter_by(is_deleted=False).all()
            tuman_l = models.Tuman.query.filter_by(is_deleted=False).all()
            return render_template("admin-respublika-create.html", form=form, respublika_list=respublika_l, viloyat_list=viloyat_l, tuman_list=tuman_l)
    else:
        return redirect(url_for("home_page"))

# viloyat
@root.route("/admin/viloyat/list", methods=["GET", "POST"])
@login_required
def admin_viloyat_list_page() -> render_template:
    if current_user.role == "ADMIN":
        respublika_l = models.Respublika.query.filter_by(is_deleted=False).all()
        viloyat_l = models.Viloyat.query.filter_by(is_deleted=False).all()
        tuman_l = models.Tuman.query.filter_by(is_deleted=False).all()
        return render_template("admin-viloyat-list.html", respublika_list=respublika_l, viloyat_list=viloyat_l, tuman_list=tuman_l)
    else:
        return redirect(url_for("home_page"))

@root.route("/admin/viloyat/update/<id>", methods=["GET", "POST"])
@login_required
def admin_viloyat_update_page(id) -> render_template:
    if current_user.role == "ADMIN":
        respublika_l = models.Respublika.query.filter_by(is_deleted=False).all()

        respublika_names = []
        for respublika in respublika_l:
            respublika_names.append(respublika.text)

        form = ViloyatForm()
        form.respublika.choices = respublika_names
        if form.validate_on_submit():
            viloyat = models.Viloyat.query.filter_by(id=id, is_deleted=False).first()
            text = form.text.data
            respublika = form.respublika.data
            respublika_t = models.Respublika.query.filter_by(text=respublika, is_deleted=False).first()
            viloyat.text = text
            viloyat.respublika_id = respublika_t.id
            models.db.session.commit()
            return redirect(url_for("admin_viloyat_list_page"))
        else:
            viloyat = models.Viloyat.query.filter_by(id=id, is_deleted=False).first()
            respublika_t = models.Respublika.query.filter_by(id=viloyat.respublika_id, is_deleted=False).first()
            form.text.data = viloyat.text
            form.respublika.data = respublika_t.text
            respublika_l = models.Respublika.query.filter_by(is_deleted=False).all()
            viloyat_l = models.Viloyat.query.filter_by(is_deleted=False).all()
            tuman_l = models.Tuman.query.filter_by(is_deleted=False).all()
            return render_template("admin-viloyat-update.html", form=form, respublika_list=respublika_l, viloyat_list=viloyat_l, tuman_list=tuman_l)
    else:
        return redirect(url_for("home_page"))

@root.route("/admin/viloyat/delete/<id>", methods=["GET", "POST"])
@login_required
def admin_viloyat_delete_page(id) -> render_template:
    if current_user.role == "ADMIN":
        viloyat = models.Viloyat.query.filter_by(id=id, is_deleted=False).first()
        viloyat.is_deleted = True
        models.db.session.commit()
        return redirect(url_for("admin_viloyat_list_page"))
    else:
        return redirect(url_for("home_page"))

@root.route("/admin/viloyat/create", methods=["GET", "POST"])
@login_required
def admin_viloyat_create_page() -> render_template:
    if current_user.role == "ADMIN":
        respublika_l = models.Respublika.query.filter_by(is_deleted=False).all()

        respublika_names = []
        for respublika in respublika_l:
            respublika_names.append(respublika.text)

        form = ViloyatForm()
        form.respublika.choices = respublika_names
        if form.validate_on_submit():
            text = form.text.data
            respublika = form.respublika.data
            respublika_t = models.Respublika.query.filter_by(text=respublika, is_deleted=False).first()
            viloyat = models.Viloyat(text, respublika_t.id, current_user.id)
            models.db.session.add(viloyat)
            models.db.session.commit()
            return redirect(url_for("admin_viloyat_list_page"))
        else:
            respublika_l = models.Respublika.query.filter_by(is_deleted=False).all()
            viloyat_l = models.Viloyat.query.filter_by(is_deleted=False).all()
            tuman_l = models.Tuman.query.filter_by(is_deleted=False).all()
            return render_template("admin-viloyat-create.html", form=form, respublika_list=respublika_l, viloyat_list=viloyat_l, tuman_list=tuman_l)
    else:
        return redirect(url_for("home_page"))

# tuman
@root.route("/admin/tuman/list", methods=["GET", "POST"])
@login_required
def admin_tuman_list_page() -> render_template:
    if current_user.role == "ADMIN":
        respublika_l = models.Respublika.query.filter_by(is_deleted=False).all()
        viloyat_l = models.Viloyat.query.filter_by(is_deleted=False).all()
        tuman_l = models.Tuman.query.filter_by(is_deleted=False).all()
        return render_template("admin-tuman-list.html", respublika_list=respublika_l, viloyat_list=viloyat_l, tuman_list=tuman_l)
    else:
        return redirect(url_for("home_page"))

@root.route("/admin/tuman/update/<id>", methods=["GET", "POST"])
@login_required
def admin_tuman_update_page(id) -> render_template:
    if current_user.role == "ADMIN":
        viloyat_l = models.Viloyat.query.filter_by(is_deleted=False).all()

        viloyat_names = []
        for viloyat in viloyat_l:
            viloyat_names.append(viloyat.text)

        form = TumanForm()
        form.viloyat.choices = viloyat_names
        if form.validate_on_submit():
            tuman = models.Tuman.query.filter_by(id=id, is_deleted=False).first()
            text = form.text.data
            viloyat = form.viloyat.data
            viloyat_t = models.Viloyat.query.filter_by(text=viloyat, is_deleted=False).first()
            tuman.text = text
            tuman.viloyat_id = viloyat_t.id
            models.db.session.commit()
            return redirect(url_for("admin_tuman_list_page"))
        else:
            tuman = models.Tuman.query.filter_by(id=id, is_deleted=False).first()
            viloyat_t = models.Viloyat.query.filter_by(id=tuman.viloyat_id, is_deleted=False).first()
            form.text.data = tuman.text
            form.vioyat.data = viloyat_t.text
            respublika_l = models.Respublika.query.filter_by(is_deleted=False).all()
            viloyat_l = models.Viloyat.query.filter_by(is_deleted=False).all()
            tuman_l = models.Tuman.query.filter_by(is_deleted=False).all()
            return render_template("admin-tuman-update.html", form=form, respublika_list=respublika_l, viloyat_list=viloyat_l, tuman_list=tuman_l)
    else:
        return redirect(url_for("home_page"))

@root.route("/admin/tuman/delete/<id>", methods=["GET", "POST"])
@login_required
def admin_tuman_delete_page(id) -> render_template:
    if current_user.role == "ADMIN":
        tuman = models.Tuman.query.filter_by(id=id, is_deleted=False).first()
        tuman.is_deleted = True
        models.db.session.commit()
        return redirect(url_for("admin_tuman_list_page"))
    else:
        return redirect(url_for("home_page"))

@root.route("/admin/tuman/create", methods=["GET", "POST"])
@login_required
def admin_tuman_create_page() -> render_template:
    if current_user.role == "ADMIN":
        viloyat_l = models.Viloyat.query.filter_by(is_deleted=False).all()

        viloyat_names = []
        for viloyat in viloyat_l:
            viloyat_names.append(viloyat.text)

        form = TumanForm()
        form.viloyat.choices = viloyat_names
        if form.validate_on_submit():
            text = form.text.data
            viloyat = form.viloyat.data
            viloyat_t = models.Viloyat.query.filter_by(text=viloyat, is_deleted=False).first()
            tuman = models.Tuman(text, viloyat_t.id, current_user.id)
            models.db.session.add(tuman)
            models.db.session.commit()
            return redirect(url_for("admin_tuman_list_page"))
        else:
            respublika_l = models.Respublika.query.filter_by(is_deleted=False).all()
            viloyat_l = models.Viloyat.query.filter_by(is_deleted=False).all()
            tuman_l = models.Tuman.query.filter_by(is_deleted=False).all()
            return render_template("admin-tuman-create.html", form=form, respublika_list=respublika_l, viloyat_list=viloyat_l, tuman_list=tuman_l)
    else:
        return redirect(url_for("home_page"))

# banner
@root.route("/admin/banner/list", methods=["GET", "POST"])
@login_required
def admin_banner_list_page() -> render_template:
    if current_user.role == "ADMIN":
        banner_l = models.Banner.query.filter_by(is_deleted=False).all()
        respublika_l = models.Respublika.query.filter_by(is_deleted=False).all()
        viloyat_l = models.Viloyat.query.filter_by(is_deleted=False).all()
        tuman_l = models.Tuman.query.filter_by(is_deleted=False).all()
        return render_template("admin-banner-list.html", banner_list=banner_l, respublika_list=respublika_l, viloyat_list=viloyat_l, tuman_list=tuman_l)
    else:
        return redirect(url_for("home_page"))

@root.route("/admin/banner/update/<id>", methods=["GET", "POST"])
@login_required
def admin_banner_update_page(id) -> render_template:
    if current_user.role == "ADMIN":
        form = BannerForm()
        if form.validate_on_submit():
            banner = models.Banner.query.filter_by(id=id, is_deleted=False).first()
            image = form.image.data
            url = form.url.data
            filename = secure_filename(image.filename)

            banner.image = "/uploads/" + filename
            banner.url = url
            image.save(os.path.join(root.config["UPLOAD_FOLDER"], filename))
            models.db.session.commit()
            return redirect(url_for("admin_banner_list_page"))
        else:
            banner = models.Banner.query.filter_by(id=id, is_deleted=False).first()
            form.url.data = banner.url
            respublika_l = models.Respublika.query.filter_by(is_deleted=False).all()
            viloyat_l = models.Viloyat.query.filter_by(is_deleted=False).all()
            tuman_l = models.Tuman.query.filter_by(is_deleted=False).all()
            return render_template("admin-banner-update.html", form=form, respublika_list=respublika_l, viloyat_list=viloyat_l, tuman_list=tuman_l)
    else:
        return redirect(url_for("home_page"))

@root.route("/admin/banner/delete/<id>", methods=["GET", "POST"])
@login_required
def admin_banner_delete_page(id) -> render_template:
    if current_user.role == "ADMIN":
        banner = models.Banner.query.filter_by(id=id, is_deleted=False).first()
        banner.is_deleted = True
        models.db.session.commit()
        return redirect(url_for("admin_banner_list_page"))
    else:
        return redirect(url_for("home_page"))

@root.route("/admin/banner/create", methods=["GET", "POST"])
@login_required
def admin_banner_create_page() -> render_template:
    if current_user.role == "ADMIN":
        form = BannerForm()
        if form.validate_on_submit():
            image = form.image.data
            url = form.url.data
            filename = secure_filename(image.filename)

            banner = models.Banner("/uploads/" + filename, url, current_user.id)
            models.db.session.add(banner)
            models.db.session.commit()
            image.save(os.path.join(root.config["UPLOAD_FOLDER"], filename))
            return redirect(url_for("admin_banner_list_page"))
        else:
            respublika_l = models.Respublika.query.filter_by(is_deleted=False).all()
            viloyat_l = models.Viloyat.query.filter_by(is_deleted=False).all()
            tuman_l = models.Tuman.query.filter_by(is_deleted=False).all()
            return render_template("admin-banner-create.html", form=form, respublika_list=respublika_l, viloyat_list=viloyat_l, tuman_list=tuman_l)
    else:
        return redirect(url_for("home_page"))

# slider
@root.route("/admin/slider/list", methods=["GET", "POST"])
@login_required
def admin_slider_list_page() -> render_template:
    if current_user.role == "ADMIN":
        slider_l = models.Slider.query.filter_by(is_deleted=False).all()
        respublika_l = models.Respublika.query.filter_by(is_deleted=False).all()
        viloyat_l = models.Viloyat.query.filter_by(is_deleted=False).all()
        tuman_l = models.Tuman.query.filter_by(is_deleted=False).all()
        return render_template("admin-slider-list.html", slider_list=slider_l, respublika_list=respublika_l, viloyat_list=viloyat_l, tuman_list=tuman_l)
    else:
        return redirect(url_for("home_page"))

@root.route("/admin/slider/update/<id>", methods=["GET", "POST"])
@login_required
def admin_slider_update_page(id) -> render_template:
    if current_user.role == "ADMIN":
        form = SliderForm()
        if form.validate_on_submit():
            slider = models.Slider.query.filter_by(id=id, is_deleted=False).first()
            image = form.image.data
            url = form.url.data
            filename = secure_filename(image.filename)

            slider.image = "/uploads/" + filename
            slider.url = url
            image.save(os.path.join(root.config["UPLOAD_FOLDER"], filename))
            models.db.session.commit()
            return redirect(url_for("admin_slider_list_page"))
        else:
            slider = models.Slider.query.filter_by(id=id, is_deleted=False).first()
            form.url.data = slider.url
            respublika_l = models.Respublika.query.filter_by(is_deleted=False).all()
            viloyat_l = models.Viloyat.query.filter_by(is_deleted=False).all()
            tuman_l = models.Tuman.query.filter_by(is_deleted=False).all()
            return render_template("admin-slider-update.html", form=form, respublika_list=respublika_l, viloyat_list=viloyat_l, tuman_list=tuman_l)
    else:
        return redirect(url_for("home_page"))

@root.route("/admin/slider/delete/<id>", methods=["GET", "POST"])
@login_required
def admin_slider_delete_page(id) -> render_template:
    if current_user.role == "ADMIN":
        slider = models.Slider.query.filter_by(id=id, is_deleted=False).first()
        slider.is_deleted = True
        models.db.session.commit()
        return redirect(url_for("admin_slider_list_page"))
    else:
        return redirect(url_for("home_page"))

@root.route("/admin/slider/create", methods=["GET", "POST"])
@login_required
def admin_slider_create_page() -> render_template:
    if current_user.role == "ADMIN":
        form = SliderForm()
        if form.validate_on_submit():
            image = form.image.data
            url = form.url.data
            filename = secure_filename(image.filename)

            slider = models.Slider("/uploads/" + filename, url, current_user.id)
            models.db.session.add(slider)
            models.db.session.commit()
            image.save(os.path.join(root.config["UPLOAD_FOLDER"], filename))
            return redirect(url_for("admin_slider_list_page"))
        else:
            respublika_l = models.Respublika.query.filter_by(is_deleted=False).all()
            viloyat_l = models.Viloyat.query.filter_by(is_deleted=False).all()
            tuman_l = models.Tuman.query.filter_by(is_deleted=False).all()
            return render_template("admin-slider-create.html", form=form, respublika_list=respublika_l, viloyat_list=viloyat_l, tuman_list=tuman_l)
    else:
        return redirect(url_for("home_page"))

# user
@root.route("/admin/user/list", methods=["GET", "POST"])
@login_required
def admin_user_list_page() -> render_template:
    if current_user.role == "ADMIN":
        user_l = models.User.query.filter_by(is_deleted=False).all()
        respublika_l = models.Respublika.query.filter_by(is_deleted=False).all()
        viloyat_l = models.Viloyat.query.filter_by(is_deleted=False).all()
        tuman_l = models.Tuman.query.filter_by(is_deleted=False).all()
        return render_template("admin-user-list.html", user_list=user_l, respublika_list=respublika_l, viloyat_list=viloyat_l, tuman_list=tuman_l)
    else:
        return redirect(url_for("home_page"))
