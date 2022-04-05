nums1 = [4,0,0,0,0,0]
m = 1

nums2 = [1,2,3,5,6]
n = 5
ctr1,ctr2=0,0
x=nums1.count(0)
while x>0:
    nums1.remove(0)
    x-=1
nums1.sort()
nums2.sort()
while ctr1<m and ctr2<n:
    if nums1[ctr1]<nums2[ctr2]:
        ctr1+=1
    elif nums1[ctr1]>nums2[ctr2]:
        nums1.insert(ctr1,nums2[ctr2])
        ctr2+=1
    elif nums1[ctr1]==nums2[ctr2]:
        nums1.insert(ctr1,nums2[ctr2])
        ctr1+=1
        ctr2+=1

while ctr2<n:
    nums1.append(nums2[ctr2])
    ctr2+=1


print(nums1)



