#Fruits into Baskets

s=['A', 'B', 'C', 'B', 'B', 'C']
window_len,max_len=0,float('-inf')
win_end=0
wind_start=0
charmap={}
for i  in range(0,len(s)):
    if s[i] in charmap:
        charmap[s[i]]+=1
    else:
        charmap[s[i]]=1
    while len(charmap)>2:
        charmap[s[wind_start]]-=1
        if charmap[s[wind_start]]==0:
            del charmap[s[wind_start]]
        wind_start=wind_start+1
    max_len = max(max_len, i - wind_start + 1)
print(max_len)