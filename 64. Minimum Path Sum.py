grid =[[1,2,3],[4,5,6]]
rows=len(grid)-1
col=len(grid[0])-1

def dp(r,c):
    if r==0 and c==0:
        return grid[r][c]
    if r<0 or c<0:
        return float('inf')
    a=dp(r-1,c)+grid[r][c]
    b=dp(r,c-1)+grid[r][c]
    return min(a,b)
print(dp(rows,col))

