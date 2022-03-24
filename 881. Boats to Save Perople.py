people=[2,2,2,3,3]
limit=6
res=[]
people.sort()
visited=[]
head=0
tail=len(people)-1

while(head<=tail):
    if people[head]+people[tail]<=limit:
        res.append([people[head],people[tail]])
        visited.append(head)
        visited.append(tail)
        head=head+1
        tail=tail-1
    else:
        tail=tail-1

for x in range(len(people)):
    if x not in visited and people[x]<=limit:
        res.append(people[x])
print(len(res))
print(res)
