class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i=0
        r=0
        ans=0
        sets=set()
        for i in range(len(s)):
            while s[i] in sets:
                sets.remove(s[r])
                r=r+1
            sets.add(s[i])
            ans=max(ans,i-r+1)
        return ans
                