arr=[1,0,0,1,0,1]
k=2
max_ones_count,window_start=0,0
max_length=float('-inf')
for window_end in range(len(arr)):
    if arr[window_end] == 1:
      max_ones_count += 1
    if (window_end - window_start + 1 - max_ones_count) > k:
      if arr[window_start] == 1:
        max_ones_count -= 1
      window_start += 1

    max_length = max(max_length, window_end - window_start + 1)
print(max_length)