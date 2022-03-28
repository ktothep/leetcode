answerKey = "FFFTTFTTFT"
k = 3

maxlen = float('-inf')
win_start, win_end = 0, 0
charmap = {}

for i in range(len(answerKey)):
    if answerKey[i] in charmap:
        charmap[answerKey[i]] += 1
    else:
        charmap[answerKey[i]] = 1
    while charmap.get("T",0)>k and   charmap.get("F",0)>k:
        charmap[answerKey[win_start]]-=1
        if charmap[answerKey[win_start]]==0:
            del charmap[answerKey[win_start]]
        win_start+=1
    maxlen=max(maxlen,sum(charmap.values()))
print(maxlen)
