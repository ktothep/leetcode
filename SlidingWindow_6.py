s="aabccbb"
k=2
charmap={}
maxfrq=0
start=0
maxlen=0
for i in range(len(s)):
    if s[i] in charmap:
        charmap[s[i]]+=1
    else:
        charmap[s[i]]=1
    maxfrq=max(maxfrq,charmap[s[i]])
    while i-start+1-maxfrq>k:
        charmap[s[start]] -= 1
        if charmap[s[start]]==0:
            del charmap[s[start]]
        start+=1
    maxlen=max(maxlen,sum((charmap.values())))
print(maxlen)