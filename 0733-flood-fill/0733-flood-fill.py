class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        from collections import deque
        q=deque()
        r=len(image)
        c=len(image[0])
        for i in range(r):
            for j in range(c):  
                if i==sr and j==sc:
                    q.append((i,j))
                    org_color=image[i][j]
                    if org_color == color:
                        return image
                    image[i][j]=color
                    break
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        while q:
            ro,co=q.popleft()
            for dr,dc in directions:
                nr=ro+dr
                nc=co+dc

                if 0<=nr<r and 0<=nc<c and image[nr][nc]==org_color:
                    image[nr][nc]=color
                    q.append((nr,nc))
                
        return image

            
            