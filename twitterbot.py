import tweepy
import random
import pandas as pd
import time

#get your codes from https://apps.twitter.com/
consumer_key = 'your_code_here'
consumer_secret = 'your_code_here'
access_token = 'your_code_here'
access_token_secret = 'your_code_here'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#change this to match your file
df = pd.read_csv('your_csv_file.csv', encoding='latin-1', error_bad_lines=False, delimiter=';')

#in my csv file the data starts from column 7 and row index one. 
#From there I read a random cell content and post that to Twitter
while True:
   readCol = random.randrange(7,len(df.columns))
   readRow = random.randrange (1,len(df.index))
   tweet = str(df.iat[readRow, readCol])

   if len(tweet) > 10 and len(tweet) < 280:
     api.update_status(tweet)
     time.sleep(10800)
   else:
     continue
