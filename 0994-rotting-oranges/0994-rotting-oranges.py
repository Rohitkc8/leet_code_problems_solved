class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        from collections import deque
        q=deque()
        minute=0
        fresh=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    q.append((i,j))
                elif grid[i][j]==1:
                    fresh+=1
        if fresh==0:
            return 0
            exit()
        while q :
            for i in range(len(q)):
                r,c=q.popleft()
                for dr,dc in directions:
                    nr=dr+r
                    nc=dc+c
                    if 0<=nr<m and 0<=nc<n and grid[nr][nc]==1:
                        q.append((nr,nc))
                        grid[nr][nc]=2
                        fresh-=1
            minute+=1
        if fresh==0:
            return minute-1
        return -1
            

                
