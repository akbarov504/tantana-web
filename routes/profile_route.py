import os
from app import root
from models import models
from datetime import datetime
from forms.profile_form import ProfileForm
from werkzeug.utils import secure_filename
from flask import render_template, redirect, url_for
from flask_login import current_user, login_required

@root.route("/profile/list/<id>", methods=["GET", "POST"])
def profile_list_page(id) -> render_template:
    profile_l = models.Profile.query.filter_by(category_id=id, is_deleted=False).all()
    respublika_l = models.Respublika.query.filter_by(is_deleted=False).all()
    viloyat_l = models.Viloyat.query.filter_by(is_deleted=False).all()
    tuman_l = models.Tuman.query.filter_by(is_deleted=False).all()
    return render_template("profile.html", profile_list=profile_l, respublika_list=respublika_l, viloyat_list=viloyat_l, tuman_list=tuman_l)

@root.route("/profile/list/res/<_respublika>", methods=["GET", "POST"])
def profile_list_respublika_page(_respublika) -> render_template:
    profile_l = models.Profile.query.filter_by(respublika=_respublika, is_deleted=False).all()
    respublika_l = models.Respublika.query.filter_by(is_deleted=False).all()
    viloyat_l = models.Viloyat.query.filter_by(is_deleted=False).all()
    tuman_l = models.Tuman.query.filter_by(is_deleted=False).all()
    return render_template("profile.html", profile_list=profile_l, respublika_list=respublika_l, viloyat_list=viloyat_l, tuman_list=tuman_l)

@root.route("/profile/list/vil/<_viloyat>", methods=["GET", "POST"])
def profile_list_viloyat_page(_viloyat) -> render_template:
    profile_l = models.Profile.query.filter_by(viloyat=_viloyat, is_deleted=False).all()
    respublika_l = models.Respublika.query.filter_by(is_deleted=False).all()
    viloyat_l = models.Viloyat.query.filter_by(is_deleted=False).all()
    tuman_l = models.Tuman.query.filter_by(is_deleted=False).all()
    return render_template("profile.html", profile_list=profile_l, respublika_list=respublika_l, viloyat_list=viloyat_l, tuman_list=tuman_l)

@root.route("/profile/list/tu/<_tuman>", methods=["GET", "POST"])
def profile_list_tuman_page(_tuman) -> render_template:
    profile_l = models.Profile.query.filter_by(tuman=_tuman, is_deleted=False).all()
    respublika_l = models.Respublika.query.filter_by(is_deleted=False).all()
    viloyat_l = models.Viloyat.query.filter_by(is_deleted=False).all()
    tuman_l = models.Tuman.query.filter_by(is_deleted=False).all()
    return render_template("profile.html", profile_list=profile_l, respublika_list=respublika_l, viloyat_list=viloyat_l, tuman_list=tuman_l)

@root.route("/profile/get/<id>", methods=["GET", "POST"])
def profile_get_page(id) -> render_template:
    respublika_l = models.Respublika.query.filter_by(is_deleted=False).all()
    viloyat_l = models.Viloyat.query.filter_by(is_deleted=False).all()
    tuman_l = models.Tuman.query.filter_by(is_deleted=False).all()
    profile = models.Profile.query.filter_by(id=id, is_deleted=False).first()
    calendars = models.Calendar.query.filter_by(profile_id=profile.id, is_deleted=False).order_by(models.Calendar.day).all()
    profile_i = models.ProfileImage.query.filter_by(profile_id=profile.id, is_deleted=False).all()
    profile_count = profile_i[0].id
    for pro in profile_i:
        if pro.id < profile_count:
            profile_count = pro.id
    now = datetime.now()
    month_name = now.strftime("%B")
    return render_template("profile-get.html", profile=profile, profile_images=profile_i, p_count=profile_count, calendar_list=calendars, month_name=month_name, respublika_list=respublika_l, viloyat_list=viloyat_l, tuman_list=tuman_l)

@root.route("/profile/create", methods=["GET", "POST"])
@login_required
def profile_create_page() -> render_template:
    respublika_l = models.Respublika.query.filter_by(is_deleted=False).all()
    viloyat_l = models.Viloyat.query.filter_by(is_deleted=False).all()
    tuman_l = models.Tuman.query.filter_by(is_deleted=False).all()
    category_l = models.ProfileCategory.query.filter_by(is_deleted=False).all()
    category_names = []
    for category in category_l:
        category_names.append(category.title)
    respublika_names = []
    for respublika in respublika_l:
        respublika_names.append(respublika.text)
    viloyat_names = []
    for viloyat in viloyat_l:
        viloyat_names.append(viloyat.text)
    tuman_names = []
    for tuman in tuman_l:
        tuman_names.append(tuman.text)
    form = ProfileForm()
    form.category.choices = category_names
    form.respublika.choices = respublika_names
    form.viloyat.choices = viloyat_names
    form.tuman.choices = tuman_names
    if form.validate_on_submit():
        title = form.title.data
        description = form.description.data
        image = form.image.data
        category = form.category.data
        images = form.images.data
        respublika = form.respublika.data
        viloyat = form.viloyat.data
        tuman = form.tuman.data
        
        filename = secure_filename(image.filename)
        category = models.ProfileCategory.query.filter_by(title=category, is_deleted=False).first()
        profile = models.Profile(title, description, "/uploads/"+filename, respublika, viloyat, tuman, category.id, current_user.id)
        models.db.session.add(profile)
        models.db.session.commit()

        image.save(os.path.join(root.config["UPLOAD_FOLDER"], filename))
        profile = models.Profile.query.filter_by(title=title, is_deleted=False, created_by=current_user.id).first()
        for im in images:
            filename = secure_filename(im.filename)
            p_im = models.ProfileImage("/uploads/"+filename, profile.id, current_user.id)
            models.db.session.add(p_im)
            models.db.session.commit()
        
            im.save(os.path.join(root.config["UPLOAD_FOLDER"], filename))

        cal = models.Calendar.query.filter_by(profile_id=None, created_by=current_user.id, is_deleted=False).all()
        for c in cal:
            c.profile_id = profile.id
            models.db.session.commit()
        return redirect(url_for("home_page"))
    else:
        category_l = models.ProfileCategory.query.filter_by(is_deleted=False).all()
        return render_template("servisman.html", form=form, respublika_list=respublika_l, viloyat_list=viloyat_l, tuman_list=tuman_l)

@root.route("/profile/edit/<id>", methods=["GET", "POST"])
@login_required
def profile_edit_page(id) -> render_template:
    respublika_l = models.Respublika.query.filter_by(is_deleted=False).all()
    viloyat_l = models.Viloyat.query.filter_by(is_deleted=False).all()
    tuman_l = models.Tuman.query.filter_by(is_deleted=False).all()
    category_l = models.ProfileCategory.query.filter_by(is_deleted=False).all()

    category_names = []
    for category in category_l:
        category_names.append(category.title)

    respublika_names = []
    for respublika in respublika_l:
        respublika_names.append(respublika.text)

    viloyat_names = []
    for viloyat in viloyat_l:
        viloyat_names.append(viloyat.text)

    tuman_names = []
    for tuman in tuman_l:
        tuman_names.append(tuman.text)
    form = ProfileForm()
    form.category.choices = category_names
    form.respublika.choices = respublika_names
    form.viloyat.choices = viloyat_names
    form.tuman.choices = tuman_names
    if form.validate_on_submit():
        profile = models.Profile.query.filter_by(id=id, is_deleted=False).first()
        title = form.title.data
        description = form.description.data
        image = form.image.data
        category = form.category.data
        images = form.images.data
        respublika = form.respublika.data
        viloyat = form.viloyat.data
        tuman = form.tuman.data
        
        filename = secure_filename(image.filename)
        category = models.ProfileCategory.query.filter_by(title=category, is_deleted=False).first()
        profile.title = title
        profile.description = description
        profile.respublika = respublika
        profile.tuman = tuman
        profile.viloyat = viloyat
        profile.image = "/uploads/"+filename
        profile.category_id = category.id
        models.db.session.commit()

        image.save(os.path.join(root.config["UPLOAD_FOLDER"], filename))
        profile_image_delete = models.ProfileImage.query.filter_by(profile_id=profile.id, is_deleted=False).all()
        for img_d in profile_image_delete:
            img_d.is_deleted = True
            models.db.session.add(img_d)
            models.db.session.commit()
        for im in images:
            filename = secure_filename(im.filename)
            p_im = models.ProfileImage("/uploads/"+filename, profile.id, current_user.id)
            models.db.session.add(p_im)
            models.db.session.commit()
    
            im.save(os.path.join(root.config["UPLOAD_FOLDER"], filename))

        return redirect(url_for("profile_get_page", id=profile.id))
    else:
        profile = models.Profile.query.filter_by(id=id, is_deleted=False).first()
        form.title.data = profile.title
        form.description.data = profile.description
        category = models.ProfileCategory.query.filter_by(id=profile.category_id, is_deleted=False).first()
        form.category.data = category.title
        form.respublika.data = profile.respublika
        form.viloyat.data = profile.viloyat
        form.tuman.data = profile.tuman
        return render_template("profile-edit.html", form=form)
