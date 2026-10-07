class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        first_pos = -1
        last_pos = -1

        # Find first position
        l = 0
        r = len(nums) - 1

        while l <= r:

            mid = (l + r) // 2

            if nums[mid] == target:
                first_pos = mid
                r = mid - 1

            elif nums[mid] < target:
                l = mid + 1

            else:
                r = mid - 1

        # Find last position
        l = 0
        r = len(nums) - 1

        while l <= r:

            mid = (l + r) // 2

            if nums[mid] == target:
                last_pos = mid
                l = mid + 1

            elif nums[mid] < target:
                l = mid + 1

            else:
                r = mid - 1

        return [first_pos, last_pos]