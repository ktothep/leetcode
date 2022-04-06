from collections import Counter

nums = [2,3,1,3,2]
res=[]
mapper = Counter(nums)
sorted_dict = dict((sorted(mapper.items(), key=lambda x:(x[1],-x[0]) )))
for k,v in sorted_dict.items():
    while v>0:
        res.append(k)
        v-=1
print(res)
