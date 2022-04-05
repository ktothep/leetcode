arr1 = [1,4,2,3]
arr2 = [-4,-3,6,10,20,30]
d = 3
res=0
flag=0
for i in range(len(arr1)):
    flag=0
    for j in range(len(arr2)):
        diff=abs(arr1[i]-arr2[j])
        if diff<=2:
            flag=1
            break
    if flag==0:
        res+=1

print(res)