s = "ppqp"
pattern = "pq"
if ''.join(sorted(s))==''.join(sorted(s)):
    print("True")
charmap = {}
win_start=0
fin=[]
res = ''.join(sorted(pattern))
print(res)
for win_end in range(len(s)):
    if s[win_end] in charmap:
        charmap[s[win_end]] += 1
    else:
        charmap[s[win_end]] = 1
    valSum=sum(charmap.values())
    if valSum>len(pattern):
        charmap[s[win_start]]-=1
        if charmap[s[win_start]]==0:
            del charmap[s[win_start]]
        win_start+=1
    res2=''.join(sorted(charmap.keys()))
    if res2==res:
        fin.append(win_start)

print(fin)