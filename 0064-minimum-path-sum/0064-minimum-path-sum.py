class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        r=len(grid)
        c=len(grid[0])
        arr=[[0]*c for i in range(r)]
        arr[0][0]=grid[0][0]

        for i in range(1,c):
            arr[0][i]=arr[0][i-1]+grid[0][i]
        for j in range(1,r):
            arr[j][0]=arr[j-1][0]+grid[j][0]
        
        for i in range(1,r):
            for j in range(1,c):
                arr[i][j]=min(arr[i][j-1],arr[i-1][j])+grid[i][j]
        return (arr[r-1][c-1])

            