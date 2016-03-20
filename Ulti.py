__author__ = 'Azad'

from app import models, db

def insert_post():

    post = models.Post(title = 'Sexy life all want')

    db.session.add(post)
    db.session.commit()



insert_post()