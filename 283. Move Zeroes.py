nums = [1,0]
n=len(nums)



slow_pointer=1
fast_pointer=0

while(fast_pointer<len(nums)):
    if nums[fast_pointer]!=nums[fast_pointer]:
        temp=nums[slow_pointer]
        nums[slow_pointer]=nums[fast_pointer]
        nums[fast_pointer]=temp
        slow_pointer+=1
    fast_pointer+=1
print(nums)
