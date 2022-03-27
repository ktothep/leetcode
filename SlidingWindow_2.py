#Smallest Subarray With a Greater Sum
nums=[2, 1, 5, 2, 3, 2]
S=7
sum_window,min_len=0,float('inf')
win_end=0
start_wind=0
for i in range(0,len(nums)):
    sum_window+=nums[i]
    if sum_window>=7:
        while sum_window>=7:
            min_len=min(min_len,len(nums[start_wind:i+1]))
            sum_window-=nums[start_wind]
            start_wind+=1
print(min_len)
