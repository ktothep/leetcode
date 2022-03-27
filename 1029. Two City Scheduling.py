from collections import OrderedDict

costs =[[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
n=len(costs)//2
sumB=0
sumA=0
costmap=[]
for c1,c2 in costs:
    costmap.append([c2-c1,c1,c2])
costmap.sort()

teamB=costmap[0:n]
teamA=costmap[n:]
print(teamB)
print(teamA)
for x in teamB:
    sumB+=x[2]
for y in teamA:
    sumA+=y[1]
print(sumA+sumB)








