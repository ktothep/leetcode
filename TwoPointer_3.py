nums=[-5, 2, -1, -2, 3]
n=len(nums)
res=[]
for x in range(0,n-2):
    left = x+1
    right = len(nums) - 2
    while left<right:
        if nums[x]+nums[left]+nums[right]==0:
            res.append([nums[x],nums[left],nums[right]])
            left+=1
            right-=1
        elif nums[x]+nums[left]+nums[right]>=0:
             right-=1
        elif nums[x]+nums[left]+nums[right]<=0:
             left+=1
print(res)


