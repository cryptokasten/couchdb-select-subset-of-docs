import json

from cloudant.client import Cloudant

DATASET = "data/export.json"
NUMBER_OF_DOCS = 1000

USER = "admin"
PASSWORD = "rawpassword"
NAME = "test"
URL = "http://127.0.0.1:5984/"

client = Cloudant(USER, PASSWORD, url=URL, connect=True)
db = client[NAME]

f = open(DATASET, "wt")

n = 0
for doc in db:
    del doc["_rev"]
    f.write(json.dumps(doc)+"\n")
    n += 1
    if n >= NUMBER_OF_DOCS:
        break

f.close()
