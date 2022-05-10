import tweepy
import configparser
import pandas as pd

# read configs
# config = configparser.ConfigParser()
# config.read('config.ini')

api_key = "PQZb1SJqLjD5RoBKhVpWdXeTZ"
api_key_secret ="YH7A0fH6pUiMEQQsyIeni03C4AAzkv9yN19e0dNEnst3GXKxFQ"

access_token = "1028537106-8bmkhgbXDNJgn7b1kOjcRHvniOab9TDh2S4KIDb"
access_token_secret = "gGp9iU4STCQJzp2uYCfzOLHxV1XLCcqHfEhga6DxCXzlp"

# authentication
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# user tweets
# user = 'veritasium'
# limit=300

# tweets = tweepy.Cursor(api.user_timeline, screen_name=user, count=200, tweet_mode='extended').items(limit)

# search tweets
keywords = '#savesoil'
limit=1000

tweets = tweepy.Cursor(api.search, q=keywords, count=100, tweet_mode='extended').items(limit)

# tweets = api.user_timeline(screen_name=user, count=limit, tweet_mode='extended')

# create DataFrame
columns = ['User', 'Tweet']
data = []

for tweet in tweets:
    data.append([tweet.user.screen_name, tweet.full_text])

df = pd.DataFrame(data, columns=columns)

print(df)