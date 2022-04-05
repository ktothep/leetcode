import collections
from collections import Counter

arr = [1,1,2,2,3,3,4,4,5,5]
target = 8
lis = set()
count = 0
con = Counter(arr)
result = 0
arr.sort()
for i in range(len(arr)-2):
    j = i + 1
    k = len(arr) - 1
    while j < k:
        count = arr[i] + arr[j] + arr[k]
        if count < target:
            j += 1
        elif count > target:
            k -= 1
        else:
            tup = (arr[i], arr[j], arr[k])
            if tup in lis:
                j += 1
                k -= 1
                continue

            lis.add(tup)

            if arr[i] == arr[j] == arr[k]:
                result += con[arr[i]] * (con[arr[i]] - 1) * (con[arr[i]] - 2) // 6
            elif arr[i] == arr[j]:
                result += con[arr[i]] * (con[arr[i]] - 1) * con[arr[k]] // 2
            elif arr[j] == arr[k]:
                result += con[arr[i]] * con[arr[j]] * (con[arr[j]] - 1) // 2
            else:
                result += con[arr[i]] * con[arr[j]] * con[arr[k]]
            j += 1
            k -= 1
print(result % (10 ** 9 + 7))