from app import root
from models import models
from flask import render_template

@root.route("/", methods=["GET", "POST"])
@root.route("/home", methods=["GET", "POST"])
def home_page() -> render_template:
    slayd_l = models.Slider.query.filter_by(is_deleted=False).all()
    slayd_count = slayd_l[0].id
    banner = models.Banner.query.filter_by(is_deleted=False).first()
    respublika_l = models.Respublika.query.filter_by(is_deleted=False).all()
    viloyat_l = models.Viloyat.query.filter_by(is_deleted=False).all()
    tuman_l = models.Tuman.query.filter_by(is_deleted=False).all()
    category_l = models.ProfileCategory.query.filter_by(is_deleted=False).all()

    for slayd in slayd_l:
        if slayd.id < slayd_count:
            slayd_count = slayd.id
    return render_template("index.html", category_list=category_l, slider_list=slayd_l, banner=banner, s_count=slayd_count, respublika_list=respublika_l, viloyat_list=viloyat_l, tuman_list=tuman_l)

# @root.errorhandler(404)
# def page_not_found(e):
#     return render_template('error/404.html'), 404
