"""
Assignment 8 Tristan Torgersen
"""

import tweepy, json, statistics
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()
all_sentiment = []  # collector for all sentiment scores
video_sentiment = []  # collector for Amazon Video tweet scores
video_tweet_list = []  # collector for Amazon Video tweets
list_as_words = []  # list for Amazon Video tweets split into words
word_freq = {}  # frequency dictionary

bearer_token = "AAAAAAAAAAAAAAAAAAAAAPGKVQEAAAAAA1vWDZw2mzOOeOc71tsokNLakXQ%3DQqptSENCyLshnZPfwSoGbUvKDbP4lbEJRfOjTotKoisOpYNxGP"
client = tweepy.Client(bearer_token)
# create query string
query = "(amazon prime) -is:retweet lang:en"
# search for tweets that match the query string criteria
tweets = client.search_recent_tweets(query=query, tweet_fields=["created_at", "author_id", "context_annotations"], max_results=100)
# write out tweets to JSON file on hard drive
with open("/Users/tristan/Downloads/tweets_assgn_08.json", "w", encoding="utf8") as outfile:
    for tweet in tweets.data:
        output = {"id": tweet.id, "author_id": tweet.author_id, "created_at": str(tweet.created_at), "text": tweet.text}
        # print(tweet.text)
        outfile.write(json.dumps(output, ensure_ascii=False) + "\n")
with open("/Users/tristan/Downloads/tweets_assgn_08.json", "r", encoding="utf8") as infile:
    for line in infile:
        tweet = json.loads(line)  # convert the JSON-formatted string to a Python dictionary
        tweet = tweet['text']  # just grab the text of the tweet
        current_sentiment = analyzer.polarity_scores(tweet)
        all_sentiment.append(current_sentiment['compound'])  # just grab the compound sentiment score
        if "video" in tweet:  # checking for tweets referring to Amazon Video
            video_tweet_list.append(tweet)  # add the tweet to the list if it includes 'video'
    for v_tweet in video_tweet_list:
        v_tweet = v_tweet.lower()  # make the tweet lower case so the stopwords will match
        v_sentiment = analyzer.polarity_scores(v_tweet)
        video_sentiment.append(v_sentiment['compound'])  # just grab the compound sentiment score
        if v_sentiment['compound'] > 0:  # only look through Amazon Video tweets with a positive sentiment score
            v_list = v_tweet.split()  # split the tweet into a list of words
            list_as_words = list_as_words + v_list  # add the words to the list
    for word in list_as_words:
        if word not in stop_words:  # get rid of stop words
            if word not in word_freq:  # add the word to the dictionary
                word_freq[word] = 1
            else:
                word_freq[word] = word_freq[word] + 1  # if the word is already in the dict then add another count for it
    word_list = list(word_freq.items())
    sorted_list = sorted(word_list, key=lambda x: x[1], reverse=True)  # sort the words from most frequent to least
    first_five = list(sorted_list)[:5]  # only print the first five words in the list
    print("These are the five most frequent words from the tweets about Amazon Video with a positive sentiment score:")
    print(first_five)

    all_tweets_mean = statistics.mean(all_sentiment)  # saving the statistics to variables
    v_tweets_mean = statistics.mean(video_sentiment)
    print("\nAverage sentiment score from all tweets:", all_tweets_mean)
    print("Average sentiment score from tweets including 'video':", v_tweets_mean)
    if all_tweets_mean > v_tweets_mean:
        print("\nThe average sentiment score from tweets referring to Amazon Video (",v_tweets_mean,") is lower than the average sentiment score from all tweets referring to Amazon (",all_tweets_mean,")")
    else:
        print("\nThe average sentiment score from tweets referring to Amazon Video (",v_tweets_mean,") is higher than the average sentiment score from all tweets referring to Amazon (",all_tweets_mean,")")


