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


consumerKey="lZdd2ppiab2xZGph5075wmOig"
consumerSecret="ahicdZr9nbuYPpJ6q39vZov9NQjNdBmGQ4ngieEHMGSZrDeODt"

accessToken="1304455384304762880-qOl2V9pnxRZHsyXb5xi6FC1XFndZrI"
accessSecret="BUQzwYAqpHlk2XLEJ4raHig5ZjffNA6yOv4NfbY7z34u3"

auth=tweepy.OAuthHandler(consumerKey,consumerSecret)
auth.set_access_token(accessToken,accessSecret)
api=tweepy.API(auth)

searchTerm=input("Enter the keyword to search about: ")
NoOfTerms=int(input("Enter how many tweets to search: "))

tweets=tweepy.Cursor(api.search,q=searchTerm).items(NoOfTerms)
