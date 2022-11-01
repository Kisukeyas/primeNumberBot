import os
from dotenv import load_dotenv
import tweepy

# .envを読み込み
load_dotenv()

client = tweepy.Client(
    consumer_key =  os.environ['consumer_key'],
    consumer_secret = os.environ['consumer_secret'],
    bearer_token = os.environ['bearer_token'],
    access_token = os.environ['access_token'],
    access_token_secret = os.environ['access_token_secret'],
)

# 素数を判定する関数
def checkPrimeNumber(Number):

    Ans = '素数ではありません'
    cnt = 0
    # 数値の全探索
    for i in range(1,Number+1):
        if Number % i == 0:
            cnt += 1
    if cnt == 2:
        Ans = '素数です'
    return Ans

tweets = client.search_recent_tweets(query='#checkprimenumber',tweet_fields=['public_metrics'],)

for tweet in tweets.data:
    if tweet.public_metrics['reply_count'] == 0:
        tweet_text = tweet.text.replace('#checkprimenumber', '')
        tweet_text = tweet_text.replace('\n', '')
        search_tweet_num = int(tweet_text)
        text_check_prime_number = checkPrimeNumber(search_tweet_num)
        client.create_tweet(text = f"{text_check_prime_number}", in_reply_to_tweet_id=tweet.id)
