class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        a=len(p)
        arr1=[0]*(26)
        arr2=[0]*(26)
        for i in p:
            arr1[ord(i)-ord('a')]+=1
        l=0
        r=0
        q=[]
        while(r<len(s)):
            arr2[ord(s[r])-ord('a')]+=1
            r=r+1
            if r==a+l:
                if arr1==arr2:
                    q.append(l)
                arr2[ord(s[l])-ord('a')]-=1
                l+=1
        return q

