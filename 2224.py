from datetime import datetime

current = "11:00"
correct = "11:01"
current_time = 60 * int(current[0:2]) + int(current[3:5])  # Current time in minutes
target_time = 60 * int(correct[0:2]) + int(correct[3:5])  # Target time in minutes
options=[1,5,15,60]
cache={}
def dp(cu,co):
    if cu in cache:
        return cache[cu]
    if cu==co:
        return 0
    if cu>co:
        return -1
    res=float('inf')
    for i in range(len(options)):
        subproblem=dp(cu+options[i],co)
        if subproblem==-1:
            continue
        res=min(1+subproblem,res)
    cache[cu]=res
    return cache[cu]
print(dp(current_time,target_time))
