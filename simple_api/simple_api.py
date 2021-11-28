from flask import Flask, request, abort
from pymongo import MongoClient
import bson.json_util
from bson.json_util import dumps
import pandas as pd
import json
from tinydb import TinyDB, Query

app = Flask(__name__)

# client = MongoClient()  # Create a Mongo client, using the default host and ports.
# db = client.nobel_prize  # Get the nobel_prize database.

# with open("./data/nobel_winners.json") as json_data:
#     data = json.load(json_data)

# convert json to DB format
db = TinyDB("test.json")
# for value in data:
#     db.insert(value)


##########################################################################################
####### if you want to check on browser, you must add this route behind initial url #######
##########################################################################################
@app.route("/api/winners")
def get_country_data():
    query_dict = {}
    for key in ["country"]:
        # Restricts our database queries to keys in this list.
        # gives us access to the arguments of the request ('?country=Australia&categor=Chemistry')
        arg = request.args.get(key)
    Q = Query()
    winners = db.search(Q.country == arg)
    if winners:
        # bson.dumps can serialize date objects and the like to JSON.
        return dumps(winners)
    abort(404)  # resource not found


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug="on")
