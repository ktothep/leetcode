num=[1,5,1]
if num[::-1]==sorted(num):
    print(sorted(num))

fin=[]
def recur(res,nums):
    if len(res)==len(num):
        fin.append(res)
        return
    for i in range(len(nums)):
        curr=nums[i]
        rem=nums[:i]+nums[i+1:]
        recur(res+[curr],rem)
recur([],num)
print(fin)
print(fin[fin.index(num)+1])
