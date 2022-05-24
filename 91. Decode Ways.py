s = "22233"

def dp(index):
    if len(s)==index:
        return 1
    a=0
    a=dp(index+1)
    b=0
    if s[index]!=0 and int(s[index:index+2])<=26 and index+2<=len(s):
        b=dp(index+2)
    return a+b





print (dp(0))