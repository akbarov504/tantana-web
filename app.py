from flask import Flask
from models.models import db, login_manager

root = Flask(__name__)
root.config['UPLOAD_FOLDER'] = "static/uploads"
root.config["SECRET_KEY"] = "342afc9ac23241fa1372f913"
root.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://akbarov:akbarov@localhost:5432/tantana"
root.config["WTF_CSRF_ENABLED"] = False
root.config["WTF_CSRF_SECRET_KEY"] = "fgkgsd23gkfsdk32fds4r3t43t43"

db.init_app(root)
login_manager.init_app(root)

with root.app_context():
    db.create_all()

if __name__ == "__main__":
    from routes.main_route import *
    from routes.auth_route import *
    from routes.admin_route import *
    from routes.profile_route import *
    from routes.calendar_route import *
    from routes.notification_route import *
    # root.register_error_handler(404, page_not_found)
    root.run(debug = True, port=8080)
