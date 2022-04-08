stones = [2,2]
stones.sort(reverse=True)
while len(stones)!=1 and len(stones)!=None:
    x=stones.pop(0)
    y=stones.pop(0)
    if x!=y:
        stones.append(x-y)
    if len(stones)==0:
        print(0)
    stones.sort(reverse=True)

print(stones[0])