class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        months=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        def convert_days(given):
            total_=0
            month=int(given[:2])
            days=int(given[3:])
            total_=days
            for i in range(month-1):
                total_+=months[i]
            return total_
        
        st_a=convert_days(arriveAlice)
        le_a=convert_days(leaveAlice)
        st_b=convert_days(arriveBob)
        le_b=convert_days(leaveBob)
        # print(st_a,le_a)
        # print(st_b,le_b)
        from_=max(st_a,st_b)
        to_=min(le_a,le_b)
        return max(0,to_-from_+1)

        
