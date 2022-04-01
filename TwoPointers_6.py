nums=[-1, 4, 2, 1, 3]
target=5
nums.sort()
res=0
for i in range(len(nums)-2):
    left = i+1
    right = len(nums) - 1
    while(left<right):
        if nums[i]+nums[left]+nums[right]<target:
            res=res+right-left
            left+=1
        else:
            right-=1

print(res)

