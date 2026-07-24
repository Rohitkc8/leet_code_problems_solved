class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        prev=intervals[0][1]
        c=0
        for i in range(1,len(intervals)):
            if intervals[i][0]<prev:
                c+=1
            else:
                prev=intervals[i][1]
        return c