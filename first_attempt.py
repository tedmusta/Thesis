import pandas as pd
import numpy as np
pip install tweepy
import tweepy


#import df
df = pd.read_csv('C:/Users/Gebruiker/Desktop/Master thesis/uselection_tweets_1jul_11nov.csv',
                 nrows= 5000,
                 sep = ';'
            )
tweet_ids = df['Id'].tolist()



# the ID of the status
id = 1278368973893951489

# fetching the status
tweet_text = []

for i in tweet_ids:
    try:
        status = api.get_status(i)
        # fetching the text attribute
        text = status.text
        tweet_text.append(text)
    except Exception as e:
        continue

print("The text of the status is : \n\n" + text)


tweet_ids_series = pd.DataFrame(tweet_text)
df_with_tweets = pd.concat([df, tweet_ids_series], axis = 1)
