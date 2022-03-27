s = "aababcabc"
window_len,max_len=0,float('-inf')
win_end=0
wind_start=0
charmap={}
count=0
for i  in range(0,len(s)):
   if s[i] in charmap:
       charmap[s[i]]+=1
   else:
       charmap[s[i]]=1
   keychar=charmap.keys()
   valchar=charmap.values()
   print(list(keychar))
   if len(keychar) == 3 and sum(valchar) == 3:
       count += 1
   while i-wind_start+1==3:
       charmap[s[wind_start]]-=1
       if charmap[s[wind_start]]==0:
           del charmap[s[wind_start]]
       wind_start+=1


print(count)