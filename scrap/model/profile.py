from mongoengine import Document, StringField

class profile(Document):
        company = StringField()
        role = StringField()