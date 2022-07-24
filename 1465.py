h = 5
w = 4
horizontalCuts =  [3]
verticalCuts =[3]
horizontalCuts.insert(0,0)
verticalCuts.insert(0,0)

horizontalCuts.append(h)
verticalCuts.append(w)
horizontalCuts.sort()
verticalCuts.sort()
max_diff_h=0
max_diff_w=0

for i in range(0,len(horizontalCuts)-1):
    max_diff_h=max(max_diff_h,abs(horizontalCuts[i+1]-horizontalCuts[i]))
for i in range(0,len(verticalCuts)-1):
    max_diff_w=max(max_diff_w,abs(verticalCuts[i+1]-verticalCuts[i]))
print(max_diff_h*max_diff_w)


