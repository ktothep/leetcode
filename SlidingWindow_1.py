nums=[2, 3, 4, 1, 5]
k=2
start=0
tail=k
res=0
while(tail<len(nums)):
    arr=nums[start:tail]
    res=max(res,sum(arr))
    start=start+1
    tail=tail+1

print(res)

#Method 2
window_sum,max_sum=0,0
win_start=0
win_end=0

for i in range(win_end,len(nums)):
    window_sum+=nums[i]
    if i==k:
        pass
    else:
      max_sum=max(max_sum,window_sum)
      window_sum=window_sum-nums[win_start]
      win_start+=1

