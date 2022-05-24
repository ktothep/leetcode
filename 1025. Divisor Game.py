n = 2
def div(a):
    for i in range(a):
        if a%i==0:
            return a
def check(n):
    if any(n%i==0 for i in range(1,n)):
        return check(n-1)
    return False
print(check(2))