class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        n=len(rooms)
        from collections import deque
        q=deque([0])

        visited=[False]*(n)
        visited[0]=True
        c=1
        while q:
            node=q.popleft()
            for i in rooms[node]:
                if not visited[i]:
                    visited[i]=True
                    c+=1
                    q.append(i)
        if c==n:
            return True
        return False