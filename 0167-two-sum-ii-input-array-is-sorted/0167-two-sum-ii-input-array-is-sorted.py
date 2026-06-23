class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dic={}
        for i in range(len(numbers)):
            p=target-numbers[i]
            if p in dic:
                m=i+1
                n=dic[p]+1
            else:
                dic[numbers[i]]=i
        return n,m