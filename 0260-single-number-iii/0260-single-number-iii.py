class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        freq={}
        for i in nums:
            freq[i]=freq.get(i,0)+1
        ans=[]
        for i,j in freq.items():
            if j==1:
                ans.append(i)
        return ans
