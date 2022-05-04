nums =[2,6,4,8,10,9,15]

nums_sorted=sorted(nums)
val=[]
for i in range(len(nums)):
    if nums[i]!=nums_sorted[i]:
        val.append(i)

print(max(val)-min(val)+1)



'''def recur(nums,index,res):
    if index==len(nums):
        return
    if nums[index]<nums[index-1]:
        temp=nums[index]
        nums[index]=nums[index-1]
        nums[index-1]=temp
        res.append(index-1)
        res.append(index)
    recur(nums,index+1,res)
    return res
result=recur(nums,1,[])
print(max(result)-min(result)+1)'''