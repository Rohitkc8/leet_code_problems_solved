class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        a=sum(apple)
        p=0
        c=0
        capacity.sort()
        capacity.reverse()
        for i in range(len(capacity)):
            p=p+capacity[i]
            if(a>p):
                c=c+1
            else:
                c=c+1
                break
        return c
    

        