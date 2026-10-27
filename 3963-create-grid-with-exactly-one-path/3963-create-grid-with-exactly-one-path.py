class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        grid=[[0]*n for  _ in range(m)]
        ans=[[0]*n for _ in range(m)]
        def dfs(r,c):
            if r>=m or c>=n or c<0 or r<0:
                return 
            if grid[r][c]!=0:
                return
            grid[r][c]="."
            if r==m-1 and c==n-1:
                for i in range(m):
                    for j in range(n):
                        if grid[i][j]==0:
                            ans[i][j]="#"
                        else:
                            ans[i][j]=grid[i][j]
                return
            dfs(r,c+1)
            dfs(r+1,c)
            
        dfs(0,0)
        result = []
        for row in ans:
            s = ""
            for ch in row:
                s = s + ch
            result.append(s)

        return result