tickets=[15,66,3,47,71,27,54,43,97,34,94,33,54,26,15,52,20,71,88,42,50,6,66,88,36,99,27,82,7,72]
k=18
t2=tickets[k+1:]

counter=0
nums=tickets[k]
x=len(([t for t in t2 if t>=tickets[k] ]))
print(x)
while nums>0:
   tickets=[t-1 for t in tickets]
   counter += len(tickets)
   tickets = [t1 for t1 in tickets if t1!=0]
   nums -= 1
print(counter-x)

