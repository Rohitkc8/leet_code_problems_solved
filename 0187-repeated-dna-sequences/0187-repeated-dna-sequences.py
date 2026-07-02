class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen=set()
        ans=set()
        l=0
        r=0
        p=[]
        while(r<len(s)):
            r+=1
            if r>10:
                l+=1
            if len(s[l:r])==10:
                if s[l:r] in seen:
                    ans.add(s[l:r])
                else:
                    print(s[l:r])
                    seen.add(s[l:r])
        return list(ans)