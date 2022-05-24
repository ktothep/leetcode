import collections

st = "pbbcggttciiippooaais"

k = 2
res = ""

#Master Piece Code
def recur(s, res, head, tail):
    if tail == len(s):
        if len(s[head:tail]) < k:
            res += s[head:tail]
        return res
    if s[head] != s[tail]:
        if len(s[head:tail]) < k:
            res += s[head:tail]
        return recur(s[:head] + s[tail:], res, 0, 1)
    else:
        if len(s[head:tail]) == k:
            return recur(s[:head] + s[tail:], res, 0, 1)
        return recur(s, res, head, tail + 1)

def check(s):
    res_map=collections.Counter(s)
    if any(x>=k for x in res_map.values()):
        return True
    else:
        return False
'''while check(st):
    st=recur(st, res, 0, 1)
else:
    print(recur(st, res, 0, 1))'''


#Two Pointer

def tp(s):
    head=0
    tail=1
    res=""
    while(tail<len(s)):
        if s[head] != s[tail]:
            if len(s[head:tail]) < k:
                res += s[head:tail]
            head=tail
            tail=head+1
        else:
            if len(s[head:tail]) == k:
                head=tail
                tail+=1
            else:
                tail+=1
    res+=s[head:]
    return res
'''while check(st):
    st=tp(st)
else:
    print(tp(st))'''
#stack
def removeDuplicates(s, k):
        st = []
        for i in s:
            if st and st[-1][0] == i:
                st[-1][1] += 1
                if st[-1][1] == k: st.pop()
            else:
                st.append([i, 1])
        return ''.join([i * j for i, j in st])

print(removeDuplicates(st,k))


