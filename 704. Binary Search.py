nums = [2,5]
target = 12
low=0
high=len(nums)-1
mid=(low+(high-low)//2)

def recur(low,high,mid):
    if nums[mid] == target:
        return mid
    if low>=high:
        return -1
    if nums[mid]>target:
        high=mid-1
        mid=(low+(high-low)//2)
        return recur(low, high, mid)
    elif  nums[mid]<target :
        low = mid+1
        mid = (low+(high-low)//2)
        return recur(low, high, mid)
print(recur(low,high,mid))