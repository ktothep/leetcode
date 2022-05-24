from functools import lru_cache

coins = [1]
target = 2

cache={}
def dp(amount):
    if amount in cache:
        return cache[amount]
    if amount==0:
        return 0
    if amount<0:
        return -1
    res=float('inf')
    for i in range(len(coins)):
        subproblem=dp(amount-coins[i])
        if subproblem==-1:
            continue
        res=min(1+subproblem,res)
        cache[amount]=res
    return   cache[amount] if amount in cache else  -1

print(dp(target))