class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        p=[]
        for i in nums:
            p.append(i**2)
        p.sort()
        return p