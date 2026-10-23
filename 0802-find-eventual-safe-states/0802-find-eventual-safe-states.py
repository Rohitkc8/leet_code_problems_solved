class Solution:
    def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:
        n=len(graph)
        outdgree=[0]*(n)
        rev=[[] for _ in range(n)]
        for i in range(len(graph)):
            outdgree[i]=len(graph[i])
            for nei in graph[i]:
                rev[nei].append(i)
        print(rev)
        
        from collections import deque
        q=deque()
        for i in range(n):
            if outdgree[i]==0:
                q.append(i)
        safe=[]
        while q:
            node=q.popleft()
            safe.append(node)
            for nei in rev[node]:
                outdgree[nei]-=1
                if outdgree[nei]==0:
                    q.append(nei)
        return sorted(safe)