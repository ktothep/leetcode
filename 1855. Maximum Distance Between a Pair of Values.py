nums1 = [2,2,2]
nums2 = [10,10,1]
n1=0
n2=0
res=0
while(n1<len(nums1) and n2<len(nums2)):
    if nums1[n1]<=nums2[n2]:
        res=max(res,n2-n1)
        n2+=1
    else:
        n1+=1
        n2=n1+1
print(res)