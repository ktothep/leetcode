from collections import Counter

s = "344644885"

def dp(index,num,lenght):
    if lenght==index:
        return 1
    if index in memo:
        return memo[index]
    if index>lenght:
        return 0
    if num in ['2','3','4','5','6','8']:
        a=dp(index+1,num,lenght)
        b=dp(index+2,num,lenght)
        c = dp(index + 3,num,lenght)
        memo[index]=a+b+c
        return memo[index]
    else:
        a = dp(index + 1,num,lenght)
        b = dp(index + 2,num,lenght)
        c = dp(index + 3,num,lenght)
        d = dp(index + 4,num,lenght)
        memo[index] = a + b + c+d
        return memo[index]


mappy=Counter(s)
res=1
memo={}
count=1

for x in range(len(s)-1):
    memo = {}
    if s[x]==s[x+1]:
        count+=1
    else:
        print(count)
        res=res*dp(0,s[x],count)
        count=1
memo={}
res=res*dp(0,s[len(s)-1],count)


print(res)
