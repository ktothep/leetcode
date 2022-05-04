words = ["a", "a"]
s = "aa"
i=0
ans=0
while i<len(s):
    ans+=words.count(s[:i+1])
    i+=1
print(ans)