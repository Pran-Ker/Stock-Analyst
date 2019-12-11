from dateutil.parser import parse
import pandas as pd
import pandas as ExcelWriter
import numpy as np
import csv


twitter_raw_filename = '/home/pran_ker/Projects/StockAnalyst/Sentiment-Stock/Nike_tweets.csv'
# reading the twitter scrapped data file
tweets = pd.read_csv(twitter_raw_filename)
# setting the column of tweets dataframe
tweets.columns = ["Twitter_ID","Tweet_ID","Timestamp","Tweet_Content"]

tweets = tweets[pd.notnull(tweets["Tweet_Content"])]

#Cleaning the Twitter data to change the format of data and make the data consistent
for index, row in tweets.iterrows():
    row["Tweet_Content"] = row["Tweet_Content"].strip('b\'')
    row["Timestamp"] = parse(row["Timestamp"]).strftime('%d/%m/%y')
    row["Timestamp"] = pd.to_datetime(row["Timestamp"])
    tweets["Timestamp"] = pd.to_datetime(tweets['Timestamp']).dt.date

# setting the column of tweets dataframe
tweets.columns = ["Twitter_ID","Tweet_ID","Date","Tweet_content"]


# converting the Date column of tweets dataframe to datetime
tweets = tweets.astype({"Date":"datetime64"})

#Writing the dataframe into Excel
output_filename = 'cleaned_twitter.xlsx'
writer = ExcelWriter(output_filename)
tweets.to_excel(writer)
writer.save()