from flask import Flask
from dotenv import load_dotenv
from .db.config import ConnectDB
load_dotenv()
app = Flask(__name__)
ConnectDB()
def async_db_query():
    return ("async await db_query")
@app.route("/get-data",methods=["GET", "POST"])
async def get_data():
    data = await async_db_query()
    return data
from scrap.api.user import user
