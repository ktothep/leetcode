piles =[9,8,7,6,5,1,2,3,4]
piles.sort(reverse=True)
a,b,c,=0,0,0
fp=0
lp=len(piles)-1
while fp<lp:
    b+=piles[fp+1]
    fp+=2
    lp-=1

print(b)
