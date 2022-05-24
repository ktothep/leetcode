n=[1,0,1,-4,-3]



def check(nums):
    for i in range(len(nums)-2):
        head = i+1
        while(head<len(nums)):
           if any(nums[head]>x and nums[i]<x for x in nums[head+1:]):
               return True
           else:
               head+=1
    return False

print(check(n))
