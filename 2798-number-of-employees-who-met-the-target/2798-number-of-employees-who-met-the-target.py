class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        c=0
        for i in range(len(hours)):
            if hours[i]>=target:
                c=c+1
            else:
                continue
        return c