#Longest Substring with Distinct Characters

s="abccde"
charmap={}
win_start=0
maxlen=float('-inf')
for i in range(len(s)):
    if s[i] in charmap:
        charmap[s[i]]+=1
    else:
        charmap[s[i]] = 1
    if len(list(charmap.keys()))!=sum(list(charmap.values())):
        charmap[s[win_start]]-=1
        if charmap[s[win_start]]==0:
            del charmap[s[win_start]]
        win_start+=1
    maxlen=max(maxlen,sum(list(charmap.values())))

print(maxlen)

