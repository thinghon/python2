from ast import parse
from gettext import find
from urllib import response
import requests
from bs4 import BeautifulSoup
import tweepy
import urllib
import urllib.parse

search = 0
t = input()
title = urllib.parse.quote(t)
url =  'https://korean.visitkorea.or.kr/search/search_list.do?keyword={}'.format(search)+str(title)
page = urllib.request.urlopen(url)
text = page.read().decode("utf8")
print(text)    
