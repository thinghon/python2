print("20224016-박소호")
import tweepy
import time
import urllib

def send_to_twitter(msg):
    consumer_key = 'tL4t3HVY1zpY4io3nuI3dTXfu'
    consumer_secret = 'tkeo890QMGRu9k5nyvkcBfeKzYdNoSqsKRhqQC6X3iPIvux4Pc'
    access_key = '1506814567347032064-CYiHUoZdzJW8gNRPjaUoB2T1JXkN9E'
    access_secret = 'fyLE3uKtWw9hqFvHUwNz4R08PmtISCXDge2mJ0s74uiIn'

    auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_key,access_secret)
    api = tweepy.API(auth)
    api.update_status(msg)
def get_price():
    page = urllib.request.urlopen("http://cs.sch.ac.kr/prices-loyalty.py")
    text = page.read().decode("utf8")
    where = text.find(">$")
    start_of_price = where + 2
    end_of_price = start_of_price + 4
    return float (text[start_of_price:end_of_price])

price_now = input('Do you want to see the price now(Y/N)?')

if price_now == "Y":
    msg = "20224016-박소호 Buy now!,price $" + str(get_price())
    send_to_twitter(msg)
else:
    price = 99.99
    while price> 4.74:
        time.sleep(30)
        price = get_price()
    msg = "20224016-박소호 Buy!,price $" + str(price)
    send_to_twitter(msg)
