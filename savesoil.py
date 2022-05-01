import pandas as pd
import numpy as np
import tweepy
import re
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
from textblob import TextBlob
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
stop_words=set(stopwords.words('english'))


# consumerKey=
# consumerSecret=

# accessToken=
# accessSecret=

# auth=tweepy.OAuthHandler(consumerKey,consumerSecret)
# auth.set_access_token(accessToken,accessSecret)
# api=tweepy.API(auth)

# searchTerm=input("Enter the keyword to search about: ")
# NoOfTerms=int(input("Enter how many tweets to search: "))

# tweets=tweepy.Cursor(api.search,q=searchTerm).items(NoOfTerms)
