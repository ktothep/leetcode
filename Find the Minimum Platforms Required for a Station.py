arrival = [9.10,1.00]
departure = [9.50,1.30]
arrival.sort()
departure.sort()
minplat=float('-inf')
ans=0
def check(arri_pointer,dep_pointer):
    global ans
    global minplat
    if dep_pointer==len(departure) or arri_pointer==len(arrival):
        return

    if arrival[arri_pointer]>=departure[dep_pointer]:
        ans=ans-1
        check(arri_pointer,dep_pointer+1)
    else:
        ans=ans+1
        minplat=max(minplat,ans)
        check(arri_pointer+1, dep_pointer)
check(0,0)
print(minplat)