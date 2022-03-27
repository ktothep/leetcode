import collections

nums =[0,1,2,3,2,5]
k = 3
table = {}
for i, v in enumerate(nums):
    idx = table.get(v, -1)
    if idx == -1 or i - idx > k:
        table[v] = i
    else:
        print(True)

print(False)




