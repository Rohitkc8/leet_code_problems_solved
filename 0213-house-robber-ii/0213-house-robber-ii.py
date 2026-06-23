class Solution:
    def rob(self, nums: List[int]) -> int:
        nums2=nums[1:]
        p=[]
        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums)
        else:
            dp1=[0]*(len(nums)-1)
            dp1[0]=nums[0]
            dp1[1]=max(nums[0],nums[1])
            for i in range(2,len(nums)-1):
                dp1[i]=max(dp1[i-2]+nums[i],dp1[i-1])
            p.append(dp1[-1])

            dp2=[0]*(len(nums2))
            dp2[0]=nums2[0]
            dp2[1]=max(nums2[0],nums2[1])
            for i in range(2,len(nums2)):
                dp2[i]=max(dp2[i-2]+nums2[i],dp2[i-1])
            p.append(max(dp2))
            return max(p)
            


