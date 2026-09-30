class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        from collections import deque
        count=0
        rows=len(grid)
        column=len(grid[0])
        q=deque()
        for i in range(rows):
            for j in range(column):
                if grid[i][j]=="1":
                    count+=1
                    q.append((i,j))
                    while q:
                        r,c=q.popleft()

                        if r+1<rows and grid[r+1][c]=="1":
                            grid[r+1][c]="0"
                            q.append((r+1,c))
                        if c+1<column and grid[r][c+1]=="1":
                            grid[r][c+1]="0"
                            q.append((r,c+1))
                        if r-1>=0 and grid[r-1][c]=="1":
                            grid[r-1][c]="0"
                            q.append((r-1,c))
                        if c-1>=0 and grid[r][c-1]=="1":
                            grid[r][c-1]="0"
                            q.append((r,c-1))
        return count
