#Longest Substring with maximum K Distinct Characters
import collections

s="araaci"
K=2
window_len,max_len=0,float('-inf')
win_end=0
wind_start=0
charmap={}
for i  in range(0,len(s)):
    charmap=collections.Counter(s[0:i+1])
    while len(charmap)>2:
        charmap[s[wind_start]]-=1
        if charmap[s[wind_start]]==0:
            del charmap[s[wind_start]]
        wind_start=wind_start+1
    max_len = max(max_len, i - wind_start + 1)

print(max_len)

