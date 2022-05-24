memo={}
nums=[1, 2, 7, 1, 5]
summ=9
def check(sum12,idx):

        if sum12 == 0:
            return 1
        if idx > len(nums)-1 or sum12<0:
            return 0


        return check(sum12-nums[idx],idx+1)+check(sum12,idx+1)


print(check(summ,0))


