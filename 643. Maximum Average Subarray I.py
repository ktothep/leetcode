nums = [1,12,-5,-6,50,3]
k = 4
win_start,win_end=0,0
summ=0
res=float('-inf')
for i in range(len(nums)):
    summ+=nums[i]
    if (i-win_start+1==k):
        res=max(res,summ)
        summ=summ-nums[win_start]
        win_start+=1
print(res/k)

