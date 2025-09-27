def wCount(word):
    wlist=[]
    for wd in text.split():
        wlist.append(wd)
    cnt=wlist.count(word)
    return cnt

f = open("C:\\Users\\박소호\\Documents\\프로그래밍1\\Imagine.txt")
text=f.read()

w='Imagine'
n=wCount(w)
print(w+":"+str(n))

wlist=["imagine","people","dreamer"]
s={}

for wd in wlist:
    n=wCount(wd)
    s[wd]=n
print(s)