from scrap.model.test_profile.ceo_profile import Data
from scrap.model.test_profile.companies_raw import CompanyData
from scrap.utils.data_cron_job import scheduler
import httpx
import requests
from bs4 import BeautifulSoup as bs4
from flask import jsonify, json
import time

page_number=0

def CreateUser(data):
    data = json.loads(data)
    new_user = Data(company=data.get('company'),role=data.get('role'))
    new_user.save()
    return "user save",200
# getUrlData func for nested CRON JObs
# async def getUrlData(url_link):
#     content=[]  # body content
#     i = 0
#     try:
#         data = await requests.get(url_link).content
#         print("after nested request")
#         soup = bs4(data, "lxml")
#         body = soup.find("body")
#         content.append(str(body))
#         new_CompanyData = CompanyData(url=url_link, body=content[i])
#         new_CompanyData.save()
#         print(content)
#     except Exception as e:
#         print("from Get URL", str(e))


async def getUrlData(url_link):
    content = []  # Body content
    async with httpx.AsyncClient() as client:
        response = await client.get(url_link)
        data = response.content
        soup = bs4(data, "lxml")
        body = soup.find("body")
        content.append(str(body))
        new_CompanyData = CompanyData(url=url_link, body=content[0])  # Use index 0 since there's only one item
        new_CompanyData.save()
        print(content)
def profile():
    page_size=2

    global page_number
    page_number +=1
    skip_value = ( page_number - 1) * page_size
    print(f'page no ..............{page_number}')
    data = Data.objects().skip(skip_value).limit(page_size)
    
    url_list=[]# declare a list of urls
    content=[]#body content

    serialized_data = [{'company':item.company,'role':item.role} for item in data]
    if(len(serialized_data)>0):
        for i in range(0,len(serialized_data)):
            name = '+'.join(serialized_data[i]['company'].split(' '))
            url=f'https://www.google.com/search?q={name}+{serialized_data[i]['role']}'
            url_list.append(url) # append in list of url

        #now send request to get Body data
        for i in range(0,len(url_list)):
            data=requests.get(url_list[i]).content
            soup = bs4(data, "lxml")
            body = soup.find("body")
            content.append(str(body))
            new_CompanyData = CompanyData(url=url_list[i],body=content[i])
            new_CompanyData.save()

        json_content = json.dumps(content)
        print(content)
        # return json_content,200
    else:

        print("Data Completed")
        # scheduler.remove_all_jobs()


# ################################### Nested Cron Jobs #################################

# def profile():
#     page_size=2
#     global page_number
#     page_number +=1
#     skip_value = ( page_number - 1) * page_size
#     print(f'page no ..............{page_number}')
#     try:
#             data = Data.objects().skip(skip_value).limit(page_size)
#             print("fghjkjl jhcvh")
#             url_list=[]# declare a list of urls
#             content=[]#body content

#             serialized_data = [{'company':item.company,'role':item.role} for item in data]
#             if(len(serialized_data)>0):
#                 for i in range(0,len(serialized_data)):
#                     name = '+'.join(serialized_data[i]['company'].split(' '))
#                     url=f'https://www.google.com/search?q={name}+{serialized_data[i]['role']}'
#                     url_list.append(url) # append in list of url
#                     start_scheduler_nested(getUrlData,3,url)
#                     # data =await requests.get(url_list[i]).content
#                     print("after nested request")
#                     soup = bs4(data, "lxml")
#                     body = soup.find("body")
#                     content.append(str(body))
#                     new_CompanyData = CompanyData(url=url_list[i], body=content[i])
#                     new_CompanyData.save()
#                     print(content)
#                     # await getUrlData(url)

#                 json_content = json.dumps(content)
#                 return "hello world"
#                 print("profile_json_content",url_list)
#                 # return json_content,200
#             else:

#                 print("Data Completed")

#                 # scheduler.remove_all_jobs()
#     except Exception as e:
#           print("Error",str(e))
          
          
# start_scheduler(profile,20)





# # Import necessary modules
# from apscheduler.schedulers.background import BackgroundScheduler
# from apscheduler.triggers.cron import CronTrigger
# import time

# # Initialize the outer scheduler
# scheduler = BackgroundScheduler()

# # Function to start the outer scheduler
# def start_scheduler(func_Scheduler, time):
#     global page_number
#     page_number += 1
#     print(f"page_number from scheduler {page_number}")
#     scheduler.add_job(func_Scheduler, trigger=CronTrigger(second=f'*/{time}'))

# # Function to start the nested scheduler
# def start_scheduler_nested(func_Scheduler, time, *args, **kwargs):
#     inner_scheduler = BackgroundScheduler()
#     inner_scheduler.add_job(func_Scheduler, trigger=CronTrigger(second=f'*/{time}'), args=args, kwargs=kwargs)
#     inner_scheduler.start()

# # Your profile function
# def profile():
#     page_size = 2
#     global page_number
#     page_number += 1
#     skip_value = (page_number - 1) * page_size
#     print(f'page no ..............{page_number}')
#     data = Data.objects().skip(skip_value).limit(page_size)

#     url_list = []  # declare a list of urls
#     content = []  # body content

#     serialized_data = [{'company': item.company, 'role': item.role} for item in data]
#     if len(serialized_data) > 0:
#         for i in range(len(serialized_data)):
#             name = '+'.join(serialized_data[i]['company'].split(' '))
#             url = f'https://www.google.com/search?q={name}+{serialized_data[i]['role']}'
#             url_list.append(url)  # append in the list of URLs

#         # now send a request to get Body data
#         for i in range(len(url_list)):
#             data = getUrlData(url_list[i])
#             start_scheduler_nested(getUrlData, 3, url_list[i])

#             # time.sleep(2)
#             # print("after nested request")
#             # soup = bs4(data, "lxml")
#             # body = soup.find("body")
#             # content.append(str(body))
#             # new_CompanyData = CompanyData(url=url_list[i], body=content[i])
#             # new_CompanyData.save()

#         json_content = json.dumps(content)
#         print(content)
#         # return json_content, 200
#     else:
#         print("Data Completed")
#         scheduler.remove_all_jobs()

# # Start the outer scheduler
# start_scheduler(profile, 20)

# # Keep the script running
# try:
#     while True:
#         time.sleep(2)
# except (KeyboardInterrupt, SystemExit):
#     # Shut down the outer scheduler gracefully on exit
#     scheduler.shutdown()
