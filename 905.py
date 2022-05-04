nums = [0,2,1,4]
head=0
tail=1
while tail<len(nums):
    if nums[tail]%2==0 and nums[head]%2!=0:
        temp=nums[head]
        nums[head]=nums[tail]
        nums[tail]=temp
        head+=1
        tail+=1
    elif nums[tail]%2!=0 and nums[head]%2==0:
        head+=1

    else:
        tail+=1
print(nums)

