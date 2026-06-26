class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        l=0
        r=0
        ans=0
        c=0
        v="aeiou"
        while(r<len(s)):
            if s[r] in v:
                c+=1
            r+=1
            if (r-l)>k:
                if s[l] in v:
                    c-=1
                l+=1
            ans=max(ans,c)
        return ans

