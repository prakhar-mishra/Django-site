import textblob
import tweepy

def perform_twitter_analysis(query):
    consumer_key = "nqwFVVxQZvfcmnF4UXq04RTo8"
    consumer_Secret = "iBPpfOZEgONS9QeNbZd2ksHFVKr7THULRKz2JyFaOWpTWo0ae1"

    access_token = "1107700709896523776-DfjEK5ZrQg3QMsFdvGWeFkyutQp7Tr"
    access_token_secret = "uIVdEAkvJNPyj5Vib1furUP7hAOvxYQ2DIXeEN7Q68dRl"

    auth = tweepy.OAuthHandler(consumer_key, consumer_Secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)
    print(query)
    public_tweets = api.search(query)

    feed_analysis = []
    print(public_tweets)
    for tweet in public_tweets:
        print(tweet.text)
        tweet_data = {}
        tweet_data['tweet'] = tweet.text
        analysis = textblob.TextBlob(tweet.text)
        print(analysis.sentiment)
        tweet_data['analysis'] = analysis.sentiment
        feed_analysis.append(tweet_data)
        # tweet_writer.writerow(tweetData)
    print("*********")
    print(feed_analysis)
    return feed_analysis

