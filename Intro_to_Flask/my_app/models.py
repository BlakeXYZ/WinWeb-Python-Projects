'''
https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database

models.py usage:

For DB management, using SQLAlchemy (friendly Object Relational Mapper or ORM)
SQLAlchemy used for many relationsal databases (SQL)
- SQLite, MySQL, and PostgresSQL
- This is extremely powerful, because you can do your development using a simple SQLite database that does not require a server, and then when the time comes to deploy the application on a production server you can choose a more robust MySQL or PostgreSQL server, without having to change your application.

User database model

'''

from datetime import datetime, timezone
from typing import Optional

import sqlalchemy as sa
import sqlalchemy.orm as so
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

from my_app import db
from my_app import login


@login.user_loader
def load_user(id):
    return db.session.get(User, int(id))

class User(UserMixin, db.Model):

    id: so.Mapped[int] =                so.mapped_column(primary_key=True)
    username: so.Mapped[str] =          so.mapped_column(sa.String(64), index=True, unique=True)
    email: so.Mapped[str] =             so.mapped_column(sa.String(120), index=True, unique=True)
    pw_hash: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))

    posts: so.WriteOnlyMapped['Post'] = so.relationship(back_populates='author')   # relationship with class Post

    def __repr__(self) -> str:
        return f'<username = {self.username}>'

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    
class Post(db.Model):

    id: so.Mapped[int] =                so.mapped_column(primary_key=True)
    body: so.Mapped[str] =              so.mapped_column(sa.String(140), index=True, unique=True)
    timestamp: so.Mapped[datetime] =    so.mapped_column(index=True, default=lambda: datetime.now(timezone.utc))
    user_id: so.Mapped[int] =           so.mapped_column(sa.ForeignKey(User.id), index=True)    # references class User: id value

    author: so.Mapped[User] = so.relationship(back_populates='posts') # relationship with class User

    def __repr__(self) -> str:
        return f'<Post = {self.body}>'
    

