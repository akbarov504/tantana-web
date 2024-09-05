from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin

db = SQLAlchemy()
login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id, is_deleted=False).first()

class User(db.Model, UserMixin):
    __tablename__ = "user"

    id = db.Column(db.Integer(), primary_key=True)
    
    full_name = db.Column(db.String(length=100), nullable=False)
    phone = db.Column(db.String(length=13), unique=True, nullable=False)
    password = db.Column(db.String(length=300), nullable=False)
    lang = db.Column(db.String(length=2), default="KR")
    role = db.Column(db.String(length=30), default="USER")

    is_deleted = db.Column(db.Boolean(), default=False)
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.now())
    created_by = db.Column(db.Integer(), db.ForeignKey("user.id"))
    updated_at = db.Column(db.DateTime(timezone=True), default=datetime.now())
    updated_by = db.Column(db.Integer(), db.ForeignKey("user.id"))
    
    def __init__(self, full_name: str, phone: str, password: str, lang: str, role: str, created_by: int) -> None:
        super().__init__()
        self.full_name = full_name
        self.phone = phone
        self.password = password
        self.lang = lang
        self.role = role
        self.created_by = created_by

    def get_id(self):
        return str(self.id)

class ProfileCategory(db.Model):
    __tablename__ = "profile_category"

    id = db.Column(db.Integer(), primary_key=True)

    title = db.Column(db.String(length=100), nullable=False)
    description = db.Column(db.String(length=300), nullable=False)

    is_deleted = db.Column(db.Boolean(), default=False)
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.now())
    created_by = db.Column(db.Integer(), db.ForeignKey("user.id"))
    updated_at = db.Column(db.DateTime(timezone=True), default=datetime.now())
    updated_by = db.Column(db.Integer(), db.ForeignKey("user.id"))
    
    def __init__(self, title: str, description: str, created_by: int) -> None:
        super().__init__()
        self.title = title
        self.description = description
        self.created_by = created_by

    def get_id(self):
        return str(self.id)
    
class Profile(db.Model):
    __tablename__ = "profile"

    id = db.Column(db.Integer(), primary_key=True)

    title = db.Column(db.String(length=100), nullable=False)
    description = db.Column(db.String(length=300), nullable=False)
    image = db.Column(db.String(length=300), nullable=False)
    category_id = db.Column(db.Integer(), db.ForeignKey("profile_category.id"))
    respublika = db.Column(db.String(length=300))
    viloyat = db.Column(db.String(length=300))
    tuman = db.Column(db.String(length=300))

    is_deleted = db.Column(db.Boolean(), default=False)
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.now())
    created_by = db.Column(db.Integer(), db.ForeignKey("user.id"))
    updated_at = db.Column(db.DateTime(timezone=True), default=datetime.now())
    updated_by = db.Column(db.Integer(), db.ForeignKey("user.id"))
    
    def __init__(self, title: str, description: str, image: str, respublika: str, viloyat: str, tuman: str, category_id: int, created_by: int) -> None:
        super().__init__()
        self.title = title
        self.description = description
        self.image = image
        self.respublika = respublika
        self.viloyat = viloyat
        self.tuman = tuman
        self.category_id = category_id
        self.created_by = created_by

    def get_id(self):
        return str(self.id)

class ProfileImage(db.Model):
    __tablename__ = "profile_image"

    id = db.Column(db.Integer(), primary_key=True)

    image = db.Column(db.String(length=300), nullable=False)
    profile_id = db.Column(db.Integer(), db.ForeignKey("profile.id"))

    is_deleted = db.Column(db.Boolean(), default=False)
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.now())
    created_by = db.Column(db.Integer(), db.ForeignKey("user.id"))
    updated_at = db.Column(db.DateTime(timezone=True), default=datetime.now())
    updated_by = db.Column(db.Integer(), db.ForeignKey("user.id"))
    
    def __init__(self, image: str, profile_id: int, created_by: int) -> None:
        super().__init__()
        self.image = image
        self.profile_id = profile_id
        self.created_by = created_by

    def get_id(self):
        return str(self.id)
    
class ProfileSave(db.Model):
    __tablename__ = "profile_save"

    id = db.Column(db.Integer(), primary_key=True)

    user_id = db.Column(db.Integer(), db.ForeignKey("user.id"))
    profile_id = db.Column(db.Integer(), db.ForeignKey("profile.id"))

    is_deleted = db.Column(db.Boolean(), default=False)
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.now())
    created_by = db.Column(db.Integer(), db.ForeignKey("user.id"))
    updated_at = db.Column(db.DateTime(timezone=True), default=datetime.now())
    updated_by = db.Column(db.Integer(), db.ForeignKey("user.id"))
    
    def __init__(self, user_id: int, profile_id: int, created_by: int) -> None:
        super().__init__()
        self.user_id = user_id
        self.profile_id = profile_id
        self.created_by = created_by

    def get_id(self):
        return str(self.id)
    
class Slider(db.Model):
    __tablename__ = "slider"

    id = db.Column(db.Integer(), primary_key=True)

    image = db.Column(db.String(length=300), nullable=False)
    url = db.Column(db.String(length=300), nullable=False)

    is_deleted = db.Column(db.Boolean(), default=False)
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.now())
    created_by = db.Column(db.Integer(), db.ForeignKey("user.id"))
    updated_at = db.Column(db.DateTime(timezone=True), default=datetime.now())
    updated_by = db.Column(db.Integer(), db.ForeignKey("user.id"))
    
    def __init__(self, image: str, url: str, created_by: int) -> None:
        super().__init__()
        self.image = image
        self.url = url
        self.created_by = created_by

    def get_id(self):
        return str(self.id)
    
class Banner(db.Model):
    __tablename__ = "banner"

    id = db.Column(db.Integer(), primary_key=True)

    image = db.Column(db.String(length=300), nullable=False)
    url = db.Column(db.String(length=300), nullable=False)

    is_deleted = db.Column(db.Boolean(), default=False)
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.now())
    created_by = db.Column(db.Integer(), db.ForeignKey("user.id"))
    updated_at = db.Column(db.DateTime(timezone=True), default=datetime.now())
    updated_by = db.Column(db.Integer(), db.ForeignKey("user.id"))
    
    def __init__(self, image: str, url: str, created_by: int) -> None:
        super().__init__()
        self.image = image
        self.url = url
        self.created_by = created_by

    def get_id(self):
        return str(self.id)

class Calendar(db.Model):
    __tablename__ = "calendar"

    id = db.Column(db.Integer(), primary_key=True)

    profile_id = db.Column(db.Integer(), db.ForeignKey("profile.id"))
    day = db.Column(db.Integer(), nullable=False)
    date = db.Column(db.String(length=30), nullable=False)
    is_free = db.Column(db.Boolean(), default=True)

    is_deleted = db.Column(db.Boolean(), default=False)
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.now())
    created_by = db.Column(db.Integer(), db.ForeignKey("user.id"))
    updated_at = db.Column(db.DateTime(timezone=True), default=datetime.now())
    updated_by = db.Column(db.Integer(), db.ForeignKey("user.id"))

    def __init__(self, profile_id: int, day: int, date: str, is_free: bool, created_by: int) -> None:
        super().__init__()
        self.profile_id = profile_id
        self.day = day
        self.date = date
        self.is_free = is_free
        self.created_by = created_by

    def get_id(self):
        return str(self.id)

class Chat(db.Model):
    __tablename__ = "chat"

    id = db.Column(db.Integer(), primary_key=True)

    from_user = db.Column(db.Integer(), db.ForeignKey("user.id"))
    to_user = db.Column(db.Integer(), db.ForeignKey("user.id"))
    status = db.Column(db.Boolean(), default=True)

    is_deleted = db.Column(db.Boolean(), default=False)
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.now())
    created_by = db.Column(db.Integer(), db.ForeignKey("user.id"))
    updated_at = db.Column(db.DateTime(timezone=True), default=datetime.now())
    updated_by = db.Column(db.Integer(), db.ForeignKey("user.id"))
    
    def __init__(self, from_user: int, to_user: int, created_by: int) -> None:
        super().__init__()
        self.from_user = from_user
        self.to_user = to_user
        self.created_by = created_by

    def get_id(self):
        return str(self.id)
    
class Message(db.Model):
    __tablename__ = "message"

    id = db.Column(db.Integer(), primary_key=True)

    chat_id = db.Column(db.Integer(), db.ForeignKey("chat.id"))
    message = db.Column(db.String(length=300), nullable=False)

    is_deleted = db.Column(db.Boolean(), default=False)
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.now())
    created_by = db.Column(db.Integer(), db.ForeignKey("user.id"))
    updated_at = db.Column(db.DateTime(timezone=True), default=datetime.now())
    updated_by = db.Column(db.Integer(), db.ForeignKey("user.id"))

    def __init__(self, chat_id: int, message: str, created_by: int) -> None:
        super().__init__()
        self.chat_id = chat_id
        self.message = message
        self.created_by = created_by

    def get_id(self):
        return str(self.id)

class Respublika(db.Model):
    __tablename__ = "respublika"

    id = db.Column(db.Integer(), primary_key=True)

    text = db.Column(db.String(length=300), nullable=False)

    is_deleted = db.Column(db.Boolean(), default=False)
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.now())
    created_by = db.Column(db.Integer(), db.ForeignKey("user.id"))
    updated_at = db.Column(db.DateTime(timezone=True), default=datetime.now())
    updated_by = db.Column(db.Integer(), db.ForeignKey("user.id"))
    
    def __init__(self, text: str, created_by: int) -> None:
        super().__init__()
        self.text = text
        self.created_by = created_by

    def get_id(self):
        return str(self.id)
    
class Viloyat(db.Model):
    __tablename__ = "viloyat"

    id = db.Column(db.Integer(), primary_key=True)

    text = db.Column(db.String(length=300), nullable=False)
    respublika_id = db.Column(db.Integer(), db.ForeignKey("respublika.id"))

    is_deleted = db.Column(db.Boolean(), default=False)
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.now())
    created_by = db.Column(db.Integer(), db.ForeignKey("user.id"))
    updated_at = db.Column(db.DateTime(timezone=True), default=datetime.now())
    updated_by = db.Column(db.Integer(), db.ForeignKey("user.id"))
    
    def __init__(self, text: str, respublika_id: int, created_by: int) -> None:
        super().__init__()
        self.text = text
        self.respublika_id = respublika_id
        self.created_by = created_by

    def get_id(self):
        return str(self.id)

class Tuman(db.Model):
    __tablename__ = "tuman"

    id = db.Column(db.Integer(), primary_key=True)

    text = db.Column(db.String(length=300), nullable=False)
    viloyat_id = db.Column(db.Integer(), db.ForeignKey("viloyat.id"))

    is_deleted = db.Column(db.Boolean(), default=False)
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.now())
    created_by = db.Column(db.Integer(), db.ForeignKey("user.id"))
    updated_at = db.Column(db.DateTime(timezone=True), default=datetime.now())
    updated_by = db.Column(db.Integer(), db.ForeignKey("user.id"))
    
    def __init__(self, text: str, viloyat_id: int, created_by: int) -> None:
        super().__init__()
        self.text = text
        self.viloyat_id = viloyat_id
        self.created_by = created_by

    def get_id(self):
        return str(self.id)
