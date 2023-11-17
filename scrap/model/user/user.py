from mongoengine import Document, StringField, IntField

class User(Document):
    name = StringField()
    age = IntField()