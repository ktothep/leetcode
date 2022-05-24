maxChoosableInteger = 10
desiredTotal = 11
nums = [i for i in range(1, maxChoosableInteger+1)]
cache={k:v for k,v in zip(range(1, maxChoosableInteger+1),range(1, maxChoosableInteger+1))}



def check(index,desiredTotal,maxChoosableInteger):
    if desiredTotal == 0:
        return True
    
    for i in range(1,maxChoosableInteger+1):
        if cache[i]==-1:
            continue
        cache[i] = -1
        if nums[index] <= desiredTotal:
            if check(index + 1, desiredTotal - i,maxChoosableInteger):
                return True
    return check(index + 1, desiredTotal,maxChoosableInteger)


print(check(0, desiredTotal,maxChoosableInteger))
