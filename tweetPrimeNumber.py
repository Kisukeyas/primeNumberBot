from datetime import datetime
from zoneinfo import ZoneInfo
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

# 日付を出す
dt_now = datetime.now(ZoneInfo("Asia/Tokyo"))
date = dt_now.strftime('%Y年%m月%d日')

# 日付の数字を取得
date_nm = int(dt_now.strftime('%Y%m%d'))
text_check_prime_number = checkPrimeNumber(date_nm)

# ツイートを投稿
client.create_tweet(text = f"{date}\n\n{date_nm}は{text_check_prime_number}")
