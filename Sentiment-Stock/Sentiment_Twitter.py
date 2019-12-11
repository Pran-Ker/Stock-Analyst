#This will connect with my twitter account and create a csv file of the Tweets with Nike in it .

import tweepy
from textblob import TextBlob
import csv

#Basic Authentication for the Tweepy API to work
consumer_key = 'MxCFeJbnN3yoSi1QZR2ubJWNQ'
consumer_secret = 'CiZaHrUDTO0Y8orlL1ipa4WKmjvDhindQVpVjtBVNRWdC4UuFG'

access_token = '1133664097227067392-R1BqTRKYI5dV7AxNDNxFihxwTdQ2U4'
access_token_secret = 'aOukDBiDtAHZzhY5B75LVtAINxXsGAWA4dPJ2LTYuzJzr'


def get_tweets(username):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    # set count to however many tweets you want
    number_of_tweets = 10000
    # get tweets
    tweets_for_csv = []

    for tweet in tweepy.Cursor(api.user_timeline, screen_name=username, tweet_mode="extended").items(number_of_tweets):
        # create array of tweet information: username, tweet id, date/time, text
        tweets_for_csv.append([username, tweet.id_str, tweet.created_at, tweet.full_text.encode("utf-8")])
        # write to a new csv file from the array of tweets
        outfile = username + "_tweets.csv"

        with open(outfile, 'w+') as file:
            writer = csv.writer(file, delimiter=',')  # Write the file
            writer.writerows(tweets_for_csv)
#As the given problem statement is on Nike
#Searching for Nike
get_tweets('Nike')