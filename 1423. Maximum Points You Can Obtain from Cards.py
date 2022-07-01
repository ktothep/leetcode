grid = [[5,0,20],
        [0,5,0],
        [6,0,2]]
rows=len(grid)
col=len(grid[0])



for i in range(rows):
    for j in range(col):
        left=i==j
        right=i+j==rows-1
        if left or right:
            if grid[i][j]==0:
                print(False)
        else:
            if grid[i][j]==0:
                print(False)







