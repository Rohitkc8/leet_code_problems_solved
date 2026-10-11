class Solution:
    def isBipartite(self, graph: list[list[int]]) -> bool:
        from collections import deque
        q=deque()
        n=len(graph)
        visited=[-1]*(n)
        for i in range(n):
            if visited[i]==-1:
                q.append(i)
                visited[i]=0
            while q:
                node=q.popleft()
                print(node)
                for nxt in graph[node]:
                    if visited[nxt]==-1:
                        if visited[node]==1:
                            visited[nxt]=0
                        else:
                            visited[nxt]=1
                        q.append(nxt)
                    elif visited[nxt]==visited[node]:
                        return False
        
        return True