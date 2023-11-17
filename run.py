# from flask import Flask
# from dotenv import load_dotenv
# import os
# load_dotenv()
# app = Flask(__name__)
# PORT=os.getenv('PORT')
# print(PORT)
# @app.route('/')
# def index():
#     return 'Hello, World!'
import asyncio

from scrap import app
if __name__ == '__main__':
    asyncio.run()