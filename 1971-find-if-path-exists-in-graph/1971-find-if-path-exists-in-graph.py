class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        from collections import deque
        q=deque()
        graph=[[] for i in range(n+1)]
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        visited=[False]*(n+1)
        q.append(source)
        visited[source]=True
        while q:
            node=q.popleft()
            if node==destination:
                return True
            
            for nxt in graph[node]:
                if not visited[nxt]:
                    visited[nxt]=True
                    q.append(nxt)
        return False
