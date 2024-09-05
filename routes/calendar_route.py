from app import root
from models import models
from datetime import datetime
from calendar import monthrange
from flask_login import current_user, login_required
from flask import render_template, redirect, url_for

@root.route("/calendar/create", methods=["GET", "POST"])
@login_required
def create_calendar_page() -> render_template:
    for i in range(0, 7):
        now = datetime.now()
        if (now.month + i) == 13:
            break
        curr_now = datetime(now.year, now.month + i, now.day, now.hour, now.minute, now.second, now.microsecond)
        day_count = monthrange(curr_now.year, curr_now.month)
        month_name = curr_now.strftime("%B")
        for d_count in range(1, day_count[1]+1):
            calendar = models.Calendar(None, d_count, month_name, True, current_user.id)
            models.db.session.add(calendar)
            models.db.session.commit()
    return redirect(url_for("profile_create_page"))

@root.route("/change-status/<calendar_id>/<profile_id>", methods=["GET", "POST"])
@login_required
def change_status_page(calendar_id, profile_id) -> render_template:
    calendar = models.Calendar.query.filter_by(id=calendar_id, is_deleted=False).first()
    calendar.is_free = not calendar.is_free
    models.db.session.commit()
    return redirect(url_for("profile_get_page", id=profile_id))
