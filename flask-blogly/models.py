"""Models for Blogly."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    app.app_context().push()
    db.app = app
    db.init_app(app)

default_img = 'https://picsum.photos/200'

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    
    first_name = db.Column(db.String(20),
                           nullable=False)
    
    last_name = db.Column(db.String(20),
                          nullable=False)
    
    image_url = db.Column(db.String(),
                          nullable=False,
                          default=default_img)

    # @classmethod
    def __repr__(cls):
        u = cls
        return f"<User id={u.id} first_name={u.first_name} last_name={u.last_name} image_url={u.image_url}>"
    
    @property
    def full_name(cls):
        return f"{cls.first_name} {cls.last_name}"