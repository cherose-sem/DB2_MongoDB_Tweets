import pymongo
from pymongo import MongoClient

client = MongoClient()
db = client.social_net

def get_all():
    for tweet in db.tweets.find():
        print(tweet)

def get_total_user_amount():
    print (len(db.tweets.distinct('user')))

def get_most_linked():
    print('?')

def get_most_mentioned():
    pipeline = [
        {'$addFields': {'words':{'$split':['$text', ' ']}}}, #spliting the text by ' '
        {'$unwind':"$words"}, #reconstruct an array of the words
        {'$match':{'words':{'$regex':"@\w+",'$options':'m'}}}, #match the @ from the words list
        {'$group':{'_id':"$words",'total':{'$sum':1}}}, #sums up the unique word
        {'$sort':{'total':-1}}, #sort the total
        {'$limit':5} #only top 5
    ]
    tweets = db.tweets.aggregate(pipeline)
    print (list(tweets))

def get_most_active():
    pipeline = [
        {'$group': {'_id': '$user', 'total': {'$sum':1}}},
        {'$sort':{'total':-1}},
        {'$limit':10}
    ]
    tweets = db.tweets.aggregate(pipeline)
    print (list(tweets))

# sad, sad face, huhu
def get_most_grumpy():
    pipeline = [
        {'$match': {'text': {'$regex': "worst$"}}},
        {'$project': {'_id': 0, 'user': 1}},
        {'$limit': 5}
    ]
    tweets = db.tweets.aggregate(pipeline)
    print (list(tweets))

# love, smileys, haha
def get_most_happy():
    pipeline = [
        {'$match': {'text': {'$regex': "love$"}}},
        {'$project': {'_id': 0, 'user': 1}},
        {'$limit': 5}
    ]
    tweets = db.tweets.aggregate(pipeline)
    print (list(tweets))

# MAIN
# get_all()

# print('How many Twitter users are in the database?')
# get_total_user_amount()
#
# print('\n-------------------------------------------------------------------------')
# print('Which Twitter users link the most to other Twitter users? (Provide the top ten.)')
# get_most_linked()
#
# print('\n-------------------------------------------------------------------------')
# print('Who are the most mentioned Twitter users? (Provide the top five.)')
# get_most_mentioned()
#
print('\n-------------------------------------------------------------------------')
print('Who are the most active Twitter users (top ten)?')
get_most_active()
#
# print('\n-------------------------------------------------------------------------')
# print('Who are the five most grumpy (most negative tweets) and the most happy (most positive tweets)? (Provide five users for each group)')
# print('MOST GRUMPY: ')
# get_most_grumpy()
# print('\n')
# print('MOST HAPPY: ')
# get_most_happy()
