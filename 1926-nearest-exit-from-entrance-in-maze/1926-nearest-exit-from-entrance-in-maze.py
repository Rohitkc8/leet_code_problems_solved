class Solution:
    def nearestExit(self, maze: list[list[str]], entrance: list[int]) -> int:
        r=len(maze)
        c=len(maze[0])
        visited=[[False]*c for _ in range(r)]
        visited[entrance[0]][entrance[1]]=True

        from collections import deque
        q=deque([(entrance[0],entrance[1],0)])
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        while q:
            ro,co,steps=q.popleft()

            for dr,dc in directions:
                nr=ro+dr
                nc=co+dc

                if 0<=nr<r and 0<=nc<c:
                    if not visited[nr][nc] and maze[nr][nc]==".":
                        if nr==0 or nr==r-1 or nc==0 or nc==c-1:
                            return steps+1
                            
                        visited[nr][nc]=True
                        q.append((nr,nc,steps+1))
        return -1




