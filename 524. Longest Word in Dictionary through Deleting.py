s="abpcplea"
dictionary=["ale","apple","monkey","plea", "abpcplaaa","abpcllllll","abccclllpppeeaaaa"]
dictionary=sorted(dictionary,reverse=True,key=lambda x:len(x))


res=float('-inf')
dummy=[]

for x in dictionary:
    i = 0
    j = 0
    while i<len(x) and j<len(s):
        if x[i]==s[j]:
            i+=1
            j+=1
        elif  x[i]!=s[j]:
            j+=1

    if  i!=0 and i==len(x):
         res = max(i, res)
         if res==len(x):
            dummy.append(x)
dummy.sort()
if len(dummy)==0:
    print("")
else:
    print(dummy[0])
