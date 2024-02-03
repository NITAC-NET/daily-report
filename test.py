import requests, json
import datetime
import tweepy
import os


API_KEY = os.environ.get("TWITTER_API_KEY")
API_SECRET = os.environ.get("TWITTER_API_SECRET_KEY")
ACCESS_TOKEN = os.environ.get("TWITTER_ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.environ.get("TWITTER_ACCESS_TOKEN")
BEARER_TOKEN = os.environ.get("BEARER_TOKEN")
"""
API_KEY = 'bYlxxW3ip3FnBL48hoK6QqhXD'
API_SECRET = "KQUkPmNGsaVphw8fFICxkiie6CjbmgE7sJSS9yCkd3KLQK3hA5"
ACCESS_TOKEN = "1749074487684087808-iQgRqT3K2sLNBVnwBmCAsDndO8tyP7"
ACCESS_TOKEN_SECRET = "5eyJQJLz530WIoMm5bzOiD5wpoQFGhnuxMoHKIBA2awPT"
BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAGvesAEAAAAAbbkCoy%2B2AwXRZQNJIw%2FGjxlDXjg%3DfXaw8poLMWdznvhvAy7nNdJXZYdPfS3zSFi9WCQtDJtlVTXchm"
"""
client = tweepy.Client(
    bearer_token=BEARER_TOKEN,
    consumer_key=API_KEY,
    consumer_secret=API_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET,
)

tweet_text = """【 Daily Report】
$("GITHUB_REPOSITORY")"""

print(BEARER_TOKEN)
client.create_tweet(text=tweet_text)
