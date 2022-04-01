nums=[1, 0, 1, 1]
target=100
n=len(nums)
res=float('inf')
for x in range(0,n-2):
    left = x+1
    right = len(nums) - 2
    while left<right:
        target_diff=target-(nums[x]+nums[left]+nums[right])
        if target_diff==0:
            res=0
        if   abs(target_diff)<abs(res) or (abs(target_diff) == abs(res) and target_diff > res):
             res=target_diff

        elif nums[x]+nums[left]+nums[right]>target:
             right-=1
        elif nums[x]+nums[left]+nums[right]<target:
             left+=1
print(target-res)


