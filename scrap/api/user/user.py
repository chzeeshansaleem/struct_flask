from scrap import app
import tracemalloc
from flask import request
from scrap.services.user import CreateUser,profile
from scrap.utils.data_cron_job import start_scheduler_nested,start_scheduler
import asyncio
@app.route('/user',methods=['POST'])
def create_user():
    data=request.data

    return CreateUser(data)
@app.route('/profile',methods=['GET'])
def ceo_profile():
    tracemalloc.start()
    
    # loop = asyncio.new_event_loop()
    # asyncio.set_event_loop(loop)
    result =start_scheduler(profile,20)
    return "scheduler start"

# async def ceo_profile():
#     tracemalloc.start()
#     try:
#         await start_scheduler(profile,20)
#         return "start_scheduler"
#     except Exception as e:
#         print("error while starting API scheduler", str(e))
#         return ("error while starting API scheduler", str(e))
   
