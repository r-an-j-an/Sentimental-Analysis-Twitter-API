import tweepy
from textblob import TextBlob
import preprocessor as p
import statistics
from typing import List


auth = tweepy.OAuthHandler('api_key','api_key_secret')
auth.set_access_token('access_key','access_key_secret')

api = tweepy.API(auth)


def get_tweets(keyword: str) -> List[str]:
    all_tweets = []
    for tweet in tweepy.Cursor(api.search_tweets, q=keyword, tweet_mode='extended', lang='en').items(10):
        all_tweets.append(tweet.full_text)
    return all_tweets


def clean_tweets(all_tweets: List[str]) -> List[str]:
    tweets_clean = []
    for tweet in all_tweets:
        tweets_clean.append(p.clean(tweet))
    return tweets_clean


def get_sentiment(all_tweets: List[str]) -> List[float]:
    sentiment_scores = []
    for tweet in all_tweets:
        blob = TextBlob(tweet)
        sentiment_scores.append(blob.sentiment.polarity)

    return sentiment_scores


def generate_average_sentiment_score(keyword: str) -> int:
    tweets = get_tweets(keyword)
    tweets_clean = clean_tweets(tweets)
    for twt in tweets_clean:
        print("Tweet", twt)
        print("\n")
    sentiment_scores = get_sentiment(tweets_clean)
    average_score = statistics.mean(sentiment_scores)
    return average_score


if __name__ == "__main__":
    print("What does the World prefer?")
    first_keyword = input()
    print("or")
    second_keyword = input()
    print("\n")

    first_score = generate_average_sentiment_score(first_keyword)
    second_score = generate_average_sentiment_score(second_keyword)
    print("\n\n\n\n")
    if(first_score > second_score):
        print("The humanity prefers", first_keyword)
    if(second_score > first_score):
        print("The humanity prefers", second_keyword)

    print("------------------------------------------------------------------------------------------------------")
    print("\n")
    print(first_keyword, "has a sentimental score of ", first_score)
    print(second_keyword, "has a sentimental score of ", second_score)
