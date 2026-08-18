class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []

        def bac(ind, sol):
            if target == sum(sol):
                ans.append(sol.copy())
                return

            if target < sum(sol):
                return

            for i in range(ind, len(candidates)):

                if i > ind and candidates[i] == candidates[i - 1]:
                    continue

                sol.append(candidates[i])
                bac(i + 1, sol)
                sol.pop()

        bac(0, [])
        return ans