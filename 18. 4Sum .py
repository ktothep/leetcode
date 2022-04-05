nums=[2, 0, -1, 1, -2, 2]
nums.sort()
target=2
n=len(nums)
mapper={}
res=[]
for y in range(len(nums)-3):
    for x in range(y+1,len(nums)-2):
        left=x+1
        right=n-1
        while(left<right):
            summ=nums[x]+nums[left]+nums[right]+nums[y]
            if summ==target:
                res.append([nums[x],nums[left],nums[right],nums[y]])
                left+=1
                right-=1
            elif summ>=target:
                right-=1
            else:
                left+=1
print(res)





