import collections

s='bbcebab'
freq=set()
map_of_s=collections.Counter(s)
deletions=0
for v in  map_of_s.values():
    if v not in freq:
        freq.add(v)
        continue
    while v  in freq:
        v-=1
        deletions += 1
        if v==0:
            break
        if  v not in freq:
            freq.add(v)
            break
print(deletions)