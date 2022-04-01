n=[1, 2, 3, 4, 6]
target=6
left=0
right=len(n)-1
res=[]
while(left<right):
    if n[left]+n[right]==target:
        res.append([left,right])
        left+=1
        right-=1
    elif n[left]+n[right]>target:
        right-=1
    elif n[left]+n[right]<target:
        left+=1
print(res)