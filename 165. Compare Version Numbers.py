version1 = "1.0.1"
version2 = "1"
version1=version1.split(".")
version2=version2.split(".")
v1ptr=0
v2ptr=0
if len(version1)>len(version2):
    while(len(version1)!=len(version2)):
        version2.append("0")
else:
    while (len(version1) != len(version2)):
        version1.append("0")


a=''.join(version1)
b=''.join(version2)


res=0

while(v1ptr<len(version1) and v2ptr<len(version2)):
    x=int(version1[v1ptr])
    y = int(version2[v2ptr])
    if x==y:
        res+=0
    if x> y:
        res+=1
        break
    if x < y:
        res -= 1
        break
    v1ptr+=1
    v2ptr+=1
print(res)

