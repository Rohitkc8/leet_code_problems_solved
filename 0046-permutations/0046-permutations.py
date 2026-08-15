class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        p=[]
        from itertools import permutations
        for i in permutations(nums):
            p.append(i)
        return p