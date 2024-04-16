from dotenv import load_dotenv
import os
import json

load_dotenv()

path = os.getenv("FILE_PATH")

with open(path) as file:
    contents = file.read()

attendees_json = json.loads(contents)

print(attendees_json)