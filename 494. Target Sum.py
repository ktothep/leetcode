count=0
nums = [1,1,1,1,1]
target = 3
def calcluate(i, nums,tempsum,actualsum):
    if i==len(nums):
        if tempsum==actualsum:
             count+=1
    else:
        calcluate(i+1,nums,tempsum+nums[i],actualsum)
        calcluate(i + 1, nums, tempsum - nums[i], actualsum)
    return count
calcluate(0,nums,0,target)
print(count)