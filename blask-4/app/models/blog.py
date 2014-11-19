from app import db


class BlogPost(db.Document):
    author = db.StringField(required=True)
    title = db.StringField(required=True, max_length=100)
    body = db.StringField(required=True)
