class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map={}
        k=-1 
        j=-1
        for i in range(len(nums)):
            rem = target-nums[i];
            if rem in map:
                k=i
                j=map[rem]
                break
            else:
                map[nums[i]]=i

        return [k,j]          

            