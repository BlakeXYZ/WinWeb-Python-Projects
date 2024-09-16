'''
https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database

models.py usage:

For DB management, using SQLAlchemy (friendly Object Relational Mapper or ORM)
SQLAlchemy used for many relationsal databases (SQL)
- SQLite, MySQL, and PostgresSQL
- This is extremely powerful, because you can do your development using a simple SQLite database that does not require a server, and then when the time comes to deploy the application on a production server you can choose a more robust MySQL or PostgreSQL server, without having to change your application.

User database model

'''

from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so
from my_app import db