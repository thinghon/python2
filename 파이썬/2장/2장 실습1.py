print("20224016-박소호")
import urllib.request
page = urllib.request.urlopen("http://cs.sch.ac.kr/prices.py")
text = page.read().decode("utf8")
print(text)
