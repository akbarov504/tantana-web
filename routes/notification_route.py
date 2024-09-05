from app import root
from models import models
from sqlalchemy import or_
from flask_login import current_user
from forms.message_form import MessageForm
from flask import render_template, redirect, url_for

@root.route("/notification/send/<id>", methods=["GET", "POST"])
def notification_send_page(id) -> render_template:
    profile = models.Profile.query.filter_by(id=id, is_deleted=False).first()
    chat = models.Chat(current_user.id, profile.created_by, current_user.id)
    models.db.session.add(chat)
    models.db.session.commit()
    cha = models.Chat.query.filter_by(status=True, created_by=current_user.id, is_deleted=False).first()
    msg = models.Message(cha.id, f"Assalomu alekum, Menga {profile.title} haqida malumot bera olasizmi?", current_user.id)
    models.db.session.add(msg)
    models.db.session.commit()
    cha.status = False
    models.db.session.commit()
    return redirect(url_for("home_page"))

@root.route("/notification/list", methods=["GET", "POST"])
def notification_list_page() -> render_template:
    chat_l = models.Chat.query.filter(or_(models.Chat.from_user==current_user.id, models.Chat.to_user==current_user.id), models.Chat.is_deleted==False).all()
    return render_template("notification.html", chat_list=chat_l)

@root.route("/notification/get/<id>", methods=["GET", "POST"])
def notification_get_page(id) -> render_template:
    chat = models.Chat.query.filter_by(id=id, is_deleted=False).first()
    form = MessageForm()
    if form.validate_on_submit():
        message = form.message.data
        msg = models.Message(chat.id, message, current_user.id)
        models.db.session.add(msg)
        models.db.session.commit()
        return redirect(url_for("notification_get_page", id=id))
    else:
        chat_l = models.Chat.query.filter(or_(models.Chat.from_user==current_user.id, models.Chat.to_user==current_user.id), models.Chat.is_deleted==False).all()
        messages = models.Message.query.filter_by(chat_id=chat.id, is_deleted=False).all()
        if current_user.id == chat.from_user:
            to_user = models.User.query.filter_by(id=chat.to_user, is_deleted=False).first()
        else:
            to_user = models.User.query.filter_by(id=chat.from_user, is_deleted=False).first()
        return render_template("chat.html", chat_list=chat_l, chat=chat, message_list=messages, to_user=to_user, form=form)
