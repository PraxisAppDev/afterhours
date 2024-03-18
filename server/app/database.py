import asyncio
import motor.motor_asyncio
from dotenv import load_dotenv
import os

load_dotenv()

class Database:
  def __init__(self):
    client = motor.motor_asyncio.AsyncIOMotorClient(os.environ["ME_CONFIG_MONGODB_URL"])
    
    # Added line to fix async testing issues
    client.get_io_loop = asyncio.get_event_loop
    
    self.db = client.get_database(os.environ["ME_CONFIG_MONGODB_DATABASE"])

  def get_collection(self, collection: str):
    return self.db.get_collection(collection)

database = Database()