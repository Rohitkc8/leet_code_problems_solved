class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        amount=amount+1
        c=len(coins)+1
        arr=[[0]*amount  for i in range(c)]
        INF=float('inf')
        
        for i in range(1,amount):
            arr[0][i]=INF
        for j in range(c):
            arr[j][0]=0
        for i in range(1,c):
            for j in range(1,amount):
                if j>=coins[i-1]:
                    arr[i][j]=min(arr[i-1][j],1+arr[i][j-coins[i-1]])
                else:
                    arr[i][j]=arr[i-1][j]
        if arr[c-1][amount-1]!=INF:
            return arr[c-1][amount-1]
        return -1
        # INF = float('inf')

        # dp = [INF] * (amount + 1)
        # dp[0] = 0

        # for coin in coins:
        #     for j in range(coin, amount + 1):
        #         dp[j] = min(dp[j], 1 + dp[j - coin])

        # if dp[amount] == INF:
        #     return -1
        # return dp[amount]