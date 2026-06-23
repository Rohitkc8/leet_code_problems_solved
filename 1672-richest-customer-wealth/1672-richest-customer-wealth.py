class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        p=[]
        for i in accounts:
            p.append(sum(i))
        return (max(p))