amount = 4
coins = [1, 2, 3]
memo=[[-1 for _ in range(amount+1)] for _ in range(len(coins))]
def dp(amount,idx):

    if idx>len(coins)-1:
        return 0
    if amount==0:
        return 1
    if amount<0:
        return 0
    if memo[idx][amount] != -1:
        return memo[idx][amount]

    memo[idx][amount]= dp(amount-coins[idx],idx)+dp(amount,idx+1)
    return  memo[idx][amount]

print(dp(4,0))