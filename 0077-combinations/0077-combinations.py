class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def bac(start, sol):
            if len(sol) == k:
                ans.append(sol.copy())
                return

            for i in range(start, n + 1):
                sol.append(i)

                bac(i + 1, sol)

                sol.pop()

        bac(1, [])

        return ans