class Solution:
    def minimumRecolors(self, b: str, k: int) -> int:
        l=0
        r=0
        max_count=float('inf')
        color_bl=0
        color_w=0
        while(r<len(b)):
            if b[r]=="W":
                color_w+=1
            else:
                color_bl+=1
            r+=1
            if (r-l)>k:
                if b[l]=="W":
                    color_w-=1
                else:
                    color_bl-=1
                l+=1
            if (r-l)>=k:
                max_count=min(max_count,color_w)
        return max_count