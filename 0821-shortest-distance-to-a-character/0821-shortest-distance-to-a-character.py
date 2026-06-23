class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        index=[]
        for i in range(len(s)):
            if s[i]==c:
                index.append((i))
        q=[]  
        for i in range((len(s))):
            p=[]
            for j in range(len(index)):
                p.append(abs(i-index[j]))
            q.append(min(p))
        return (q)

            