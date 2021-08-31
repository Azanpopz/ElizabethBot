#Kiitu
import asyncio
import sys

from motor import motor_asyncio
from YoneRobot import DB_URI 
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError
from Elizabeth.conf import get_int_key, get_str_key


DB_PORT = get_int_key("27017")
DB_URI = get_str_key("DB_URI")
DB = "DaisyX"


client = MongoClient()
client = MongoClient(DB_URI, DB_PORT)[DB]
motor = motor_asyncio.AsyncIOMotorClient(DB_URI, DB_PORT)
db = motor[DB]
db = client["Elizabeth"]
try:
    asyncio.get_event_loop().run_until_complete(motor.server_info())
except ServerSelectionTimeoutError:
    sys.exit(log.critical("Can't connect to mongodb! Exiting..."))
