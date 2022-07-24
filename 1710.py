boxTypes = [[1,3],[2,2],[3,1]]
truckSize = 10
boxTypes=sorted(boxTypes,key=lambda x:(-x[1]))
amt=0
for x in boxTypes:
    truckSize-=x[0]
    if truckSize>=0:
        amt += x[0] * x[1]
        if truckSize==0:
            break
    if truckSize<0:
       amt+=(x[0]-abs(truckSize))*x[1]
       break
print(amt)

