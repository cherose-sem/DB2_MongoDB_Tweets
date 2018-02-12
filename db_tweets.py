import pymongo
from pymongo import MongoClient

client = MongoClient()
db = client.social_net


def get_total_user_amount():
    print (len(db.tweets.distinct('user')))

get_total_user_amount()
