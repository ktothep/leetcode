n=2

def dp(index):
    if index==1:
        return 2
    if index==0:
        return 1

    return (dp(index-2)+dp(index-1))

print((dp(3))**2)