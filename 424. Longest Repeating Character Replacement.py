answerKey = "ABCDE"
k = 1

maxlen = float('-inf')
win_start, win_end = 0, 0
charmap = {}
maxRepeatLetterCount=0
for i in range(len(answerKey)):
    if answerKey[i] in charmap:
        charmap[answerKey[i]] += 1
    else:
        charmap[answerKey[i]] = 1
    maxRepeatLetterCount = max(maxRepeatLetterCount, charmap[answerKey[i]])

    while (i-win_start+1-maxRepeatLetterCount)>k:
        charmap[answerKey[win_start]]-=1
        if charmap[answerKey[win_start]]==0:
            del charmap[answerKey[win_start]]
        win_start+=1
    maxlen=max(maxlen,sum(charmap.values()))
print(maxlen)
