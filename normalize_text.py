import pandas as pd
import numpy as np
import re
import contractions
import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt')
from nltk.corpus import stopwords
nltk.download('stopwords')
import string
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
from nltk.stem.snowball import SnowballStemmer
from emoji import demojize


def replace_retweet(tweet, default_replace=""):
  tweet = re.sub("^RT\s+", default_replace, tweet)
  return tweet

def replace_user(tweet, default_replace="twitteruser"):
  tweet = re.sub("\B@\w+", default_replace, tweet)
  return tweet

def replace_url(tweet, default_replace=""):
  tweet = re.sub('(http|https):\/\/\S+', default_replace, tweet)
  return tweet

def replace_hashtag(tweet, default_replace=""):
  tweet = re.sub('#+', default_replace, tweet)
  return tweet

def to_lowercase(tweet):
  return tweet.lower()

def word_repetition(tweet):
  tweet = re.sub(r'(.)\1+', r'\1\1', tweet)
  return tweet

def punct_repetition(tweet, default_replace=""):
  tweet = re.sub(r'[\?\.\!]+(?=[\?\.!])', default_replace, tweet)
  return tweet

def fix_contractions(tweet):
  return contractions.fix(tweet)

def tokenize(tweet):
  tokens = word_tokenize(tweet)
  return tokens

def demojize_tweet(tweet):
    tweet = demojize(tweet)
    return tweet


stop_words = set(stopwords.words('english'))
# print(stop_words)

def custom_tokenize(tweet, keep_punct = False, keep_alnum = False, keep_stop = False):
  token_list = word_tokenize(tweet)
    
  if not keep_punct:
    token_list = [token for token in token_list if token not in string.punctuation]
        
  if not keep_alnum:
    token_list = [token for token in token_list if token.isalpha()]
    
  if not keep_stop:
    stop_words = set(stopwords.words('english'))
    stop_words.discard('not')
    token_list = [token for token in token_list if not token in stop_words]
        
          
    
    return token_list


porter_stemmer = PorterStemmer()
lancaster_stemmer = LancasterStemmer()
snowball_stemmer = SnowballStemmer('english')

def stem_tokens(tokens, stemmer):
  token_list = []
  for token in tokens:
      token_list.append(stemmer.stem(token))
  return token_list


def process_tweet(tweet, verbose=False):
    # replace retweet
  tweet = replace_retweet(tweet, default_replace="")
  # replace user tag
  tweet = replace_user(tweet, default_replace="twitteruser")
  # replace url
  tweet = replace_url(tweet, default_replace="")
  # replace hashtag
  tweet = replace_hashtag(tweet, default_replace="")
  
  ## Word Features
    # lower case
  tweet = to_lowercase(tweet)
    # replace contractions
  tweet = fix_contractions(tweet)
    # replace punctuation repetition
  tweet = punct_repetition(tweet, default_replace="")
    # replace word repetition
  tweet = word_repetition(tweet)
    # replace emojis
  tweet = demojize_tweet(tweet)
  if verbose: print("Post Word processing tweet: {}".format(tweet))

  ## Tokenization & Stemming
    # tokenize
  tokens = custom_tokenize(tweet, keep_alnum=True)
    # define stemmer
    # stem tokens
  stem = stem_tokens(tokens, SnowballStemmer("english"))
  return stem
