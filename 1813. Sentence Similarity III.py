sentence1="qbaVXO Msgr aEWD v ekcb"
sentence2="Msgr aEWD ekcb"
if len(sentence2)>len(sentence1):
    s1 = sentence2.split(" ")
    s2 = sentence1.split(" ")
else:
    s1 = sentence1.split(" ")
    s2 = sentence2.split(" ")

if len(s1)==len(s2):
    print("True")
if len(s1)!=len(s2) and s1[0]==s2[0]:
    print("Ture")
n1 = 0
n2 = 0
res={}
while (n1 < len(s1) and n2 < len(s2)   ):
    if s1[n1]==s2[n2]:
          n1+=1
          n2+=1
    else:
        if len(s1)>len(s2):
            res[n1]= s1[n1]
            n1+=1
        else:
            res[n2] = s2[n2]
            n2+=1


for key,value in res.items():
    s2.insert(key,value)

if ' '.join(s1)==' '.join(s2):
    print("Ture")
else:
    print("False")




print(res)



