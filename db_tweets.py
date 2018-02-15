import pymongo
from pymongo import MongoClient

client = MongoClient()
db = client.social_net

def get_all():
    for tweet in db.tweets.find():
        print(tweet)

def get_total_user_amount():
    return (len(db.tweets.distinct('user'))) #gets the length of the distinct users

def get_most_linked():
    pipeline = [
        {'$match':{'text':{'$regex':"@\w+"}}}, # check a match to '@..' from the property 'text'
        {'$addFields': {"mentions":1}}, # creating a field for no. of mentions
        {'$group':{"_id":"$user", "mentions":{'$sum':1}}}, # increment the no. of mentions by each unique users mentioned
        {'$sort':{"mentions":-1}}, #sort by mentions
        {'$limit':10}] # get top 10
    tweets = db.tweets.aggregate(pipeline)
    return(list(tweets))

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
    return (list(tweets))

def get_most_active():
    pipeline = [
        {'$group': {'_id': '$user', 'total': {'$sum':1}}}, # group by unque users and increment based on number of tweets
        {'$sort':{'total':-1}}, # sort
        {'$limit':10} # top 10
    ]
    tweets = db.tweets.aggregate(pipeline)
    return (list(tweets))

def get_most_grumpy():
    pipeline = [
        {'$match': {'text': {'$regex': "worst|wtf|damn|angry|pissed|mad"}}}, # find the match on the text property
        {'$group':{'_id':"$user", 'emotion': {'$avg': "$polarity"}, 'total_negative_tweets': {'$sum': 1}}}, # sum up the total negative tweets based on users
        {'$sort':{ 'emotion': 1, 'total_negative_tweets':-1}}, # sort
        {'$limit': 5} # top 5
    ]
    tweets = db.tweets.aggregate(pipeline)
    return (list(tweets))

def get_most_happy():
    pipeline = [
        {'$match': {'text': {'$regex': "love|nice|good|great|amazing|happy"}}}, # find the match on the text property
        {'$group':{'_id':"$user", 'emotion': {'$avg': "$polarity"}, 'total_positive_tweets': {'$sum': 1}}}, # sum up the total positive tweets based on users
        {'$sort':{ 'emotion': -1, 'total_positive_tweets':-1}}, #sort
        {'$limit': 5} # top 5
    ]
    tweets = db.tweets.aggregate(pipeline)
    return (list(tweets))

def print_list(list):
    for el in list:
        print(el)

# MAIN
# get_all()

print('How many Twitter users are in the database?')
print(get_total_user_amount() , 'Twitter users')

print('\n-------------------------------------------------------------------------')
print('Which Twitter users link the most to other Twitter users? (Provide the top ten.)')
print_list(get_most_linked())

print('\n-------------------------------------------------------------------------')
print('Who are the most mentioned Twitter users? (Provide the top five.)')
print_list(get_most_mentioned())

print('\n-------------------------------------------------------------------------')
print('Who are the most active Twitter users (top ten)?')
print_list(get_most_active())

print('\n-------------------------------------------------------------------------')
print('Who are the five most grumpy (most negative tweets) and the most happy (most positive tweets)? (Provide five users for each group)')
print('MOST GRUMPY: ')
print_list(get_most_grumpy())
print('\n')
print('MOST HAPPY: ')
print_list(get_most_happy())
