class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        l = 0

        stack = []

        for i in s:
            if i == "(":
                if l > 0:
                    stack.append(i)
                l += 1

            else:
                l -= 1
                if l > 0:
                    stack.append(i)
         

        return "".join(stack)