n=7
def recur(idx,left,right):
    if idx==0:
        return
    recur(idx-2,left.append([1]),right)
    recur(idx-2,left,right.append([1]))
recur(7,[],[])
