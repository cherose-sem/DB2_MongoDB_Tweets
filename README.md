
### Assignment 2 - Analysis of Twitter Data
_Your task is to implement a small database application, which imports a dataset of Twitter tweets from the CSV file into database._

_Your application has to be able to answer queries corresponding to the following questions:_

1. _How many Twitter users are in the database?_

2. _Which Twitter users link the most to other Twitter users? (Provide the top ten.)_

3. _Who is are the most mentioned Twitter users? (Provide the top five.)_

4. _Who are the most active Twitter users (top ten)?_

5. _Who are the five most grumpy (most negative tweets) and the most happy (most positive tweets)? (Provide five users for each group)_

_Your application can be written in the language of your choice. It must have a form of UI but it is not important if it is an API, a CLI UI, a GUI, or a Web-based UI._

_You present your system's answers to the questions above in a Markdown file on your Github account. That is, you hand in this assignment via Github, with one hand-in per group. Push your solution, source, code, and presentation of the results to a Github repository per group and push a link to your solution in the hand-in area._

### Setup
This program was made in Python. 
1. See instructions here in getting the data and stored in MongoDB: https://github.com/datsoftlyngby/soft2018spring-databases-teaching-material/blob/master/lecture_notes/02-Intro_to_MongoDB.ipynb (_Make sure your database is up and running_)
2. `git clone https://github.com/cph-cs241/DB2_MongoDB_Tweets.git`
3. `python -m pip install pymongo`
4. To run: `python db_tweets.py` _It may take a while :-)_

### Solution
![image](https://user-images.githubusercontent.com/16150075/36120297-05ccfb40-1043-11e8-8e90-40a90dfbf298.png)

The following functions corresponds to the questions above:
1. get_total_user_amount
2. get_most_linked
3. get_most_mentioned
4. get_most_active
5. get_most_grumpy & get_most_happy
