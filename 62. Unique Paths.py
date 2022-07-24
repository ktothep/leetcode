m = 3
n = 7
arr=[[-1 for y in range(n)]for x in range(m)]
def dp(row,col):
    if row==0 and col==0:
        return 1
    if row<0 or col<0:
        return 0

    a=dp(row-1,col)
    b=dp(row,col-1)
    arr[row][col]= a+b
    return arr[row][col]
print(dp(m-1,n-1))
'''Tbaulation
 arr=[[0 for y in range(n)]for x in range(m)]
            arr[0][0]=1
            for i in range(m):
                for j in range(n):
                    if i ==0 and j==0:
                        arr[0][0]=1
                    elif i>=1 or j>=1:
                        arr[i][j]=arr[i-1][j]+arr[i][j-1]
            return (arr[m-1][n-1])'''