matrix = [[5],[6]]

target = 6
size=len(matrix[0])-1
for i in range(len(matrix)):
    if target<matrix[i][0] or target>matrix[i][size]:
        continue
    else:
        low=0
        high=size

        while(low<high):
            mid = (high - low) // 2
            if matrix[i][mid]==target:
                print(True)
            elif matrix[i][mid]<target:
                high=mid-1
            else:
                low=mid+1



