class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: list[list[int]]) -> list[int]:
        indgree=[0]*(n)
        graph=[[] for i in range(n)]
        for a,b in edges:
            graph[a].append(b)
            indgree[b]+=1
        from collections import deque
        q=deque()
        for i in range(n):
            if indgree[i]==0:
                q.append(i)
        ans=list(q)
        while q:
            node=q.popleft()
            for nei in graph[node]:
                indgree[nei]-=1
                if indgree[nei]==0:
                    q.append(nei)
        return ans
        
        