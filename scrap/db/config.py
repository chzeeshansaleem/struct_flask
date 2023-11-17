from mongoengine import connect
import os
db_name = os.getenv('DB_NAME')
db_host = os.getenv('DB_HOST')
#connct to the database
def ConnectDB():

    connect(db=db_name, host=db_host)