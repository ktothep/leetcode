s="karana"

def dp(left,right,word):
    count=0
    while left>=0 and right<len(word) and word[left]==word[right]:
        print(word[left:right+1])
        count+=1
        left-=1
        right+=1
    return count
res=0
for i in range(len(s)):
    res+=dp(i,i+1,s)
    res += dp(i, i, s)
print(res)
