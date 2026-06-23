class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        p=0
        for i in nums:
            c=0
            while(i>0):
                i=i//10
                c=c+1
            if c%2==0:
                p=p+1
        return p
