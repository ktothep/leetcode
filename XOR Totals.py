nums = [3,4,5,6,7,8]
ans=[]
def performXOR(nums):

    res=0
    for x in range(len(nums)):
        res=res^nums[x]
    return res

def subsets(n, res):
    if len(n)==0:
        return
    for i in range(len(n)):
        res.append(n[i])
        ans.append(performXOR(res))
        subsets(n[i+1:],res)
        res.pop()
subsets(nums,[])
print(sum(ans))

