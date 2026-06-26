class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, t: int) -> int:
        l=0
        r=0
        c=0
        sum_=0
        while(r<len(arr)):
            sum_+=arr[r]
            r+=1
            if r-l>k:
                sum_=sum_-arr[l]
                l+=1
            if sum_/k>=t and r-l>=k:
                c+=1
        return c
