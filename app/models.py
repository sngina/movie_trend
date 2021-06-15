from flask_login import UserMixin
from . import db




class Movie:

 pass

class Review(db.Model):

    pass

class User(UserMixin,db.Model):

    pass


class Role(db.Model):

    pass