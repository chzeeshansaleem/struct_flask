from mongoengine import Document, StringField

class Data(Document):
    company = StringField()
    role = StringField()