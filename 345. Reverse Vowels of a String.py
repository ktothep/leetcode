temp = "aA"
s=[]
for x in temp:
    s.append(x)
start=0
end=len(s)-1
vowels=['a','i','e','o','u','A','I','E','O','U']
while(start<end):
    if s[start] not in vowels:
        start+=1
    if s[end] not in vowels:
        end-=1
    if s[start]  in vowels and s[end] in vowels:
        temp=s[start]
        s[start]=s[end]
        s[end]=temp
        start+=1
        end-=1

print(''.join(s))