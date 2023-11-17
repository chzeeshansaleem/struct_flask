from mongoengine import Document, StringField,DateTimeField

class CompanyData(Document):
    url = StringField()
    body = StringField()
    # updated = DateTimeField()