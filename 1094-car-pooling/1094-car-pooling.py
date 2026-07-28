class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        arr=[0]*(10000)
        for c,i,o in trips:
            arr[i]+=c
            arr[o]-=c
        t=0
        for i in arr:
            t+=i
            if t>capacity:
                return False
        return True
        

