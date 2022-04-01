arr=[1,1,1,2,2,3]
next_non_duplicate = 2
k=0
i = 2
while (i < len(arr)):
    if arr[next_non_duplicate - 2] != arr[i] :
        arr[next_non_duplicate] = arr[i]
        next_non_duplicate +=1

    i += 1

print(next_non_duplicate)
print(arr[:next_non_duplicate])
