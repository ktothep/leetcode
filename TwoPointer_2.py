arr=[2, 3, 3, 3, 6, 9, 9]
next_non_duplicate = 1

i = 0
while (i < len(arr)):
    if arr[next_non_duplicate - 1] != arr[i]:
        arr[next_non_duplicate] = arr[i]
        next_non_duplicate += 1
    i += 1

print(next_non_duplicate)
