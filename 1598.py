logs = ["./","wz4/","../","mj2/","../","../","ik0/","il7/"]

flag=0
for c in logs:
    if c=='../':
        if flag==0:
            pass
        else:
            flag-=1
    elif c== './':
         pass
    else:
        flag+=1
print(flag)

