class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        p=correct.split(":")
        tar=int(p[0])*60+int(p[1])
        q=current.split(":")
        giv=int(q[0])*60+int(q[1])
        main=(tar-giv)+1
        inf=10**9
        arr=[[inf]*main for _ in range(5)]
        ele=[1,5,15,60]
        for i in range(len(ele)+1):
            arr[i][0]=0
        for i in range(1,len(ele)+1):
            for j in range(1,main):
                if j>=ele[i-1]:
                    arr[i][j]=min(arr[i-1][j],1+arr[i][j-ele[i-1]])
                else:
                    arr[i][j]=arr[i-1][j]
        return arr[len(ele)][main-1]
