class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n=len(obstacleGrid[0])
        m=len(obstacleGrid)
        arr=[[0]*n for i in range(m)]
        for i in range(m):
            if obstacleGrid[i][0]==1:
                break
            arr[i][0]=1
        for j in range(n):
            if obstacleGrid[0][j]==1:
                break
            arr[0][j]=1
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j]==1:
                    continue
                else:
                    arr[i][j]=arr[i][j-1]+arr[i-1][j]
        return arr[m-1][n-1]
