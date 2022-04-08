nums=[2,0,2,1,1,0]
slowpointer=0
fastpointer=len(nums)-1
k=0

while(k<fastpointer):
    if nums[k]==0:
        nums[slowpointer],nums[k]=nums[k],nums[slowpointer]
        k += 1
        slowpointer+=1
    elif nums[k]==1:
        k+=1
    else:
        nums[fastpointer], nums[k] = nums[k], nums[fastpointer]
        k+=1
        fastpointer-=1

print(nums)

