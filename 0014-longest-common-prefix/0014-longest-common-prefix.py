class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        min_len = 10000
        for s in strs:
            if len(s) < min_len:
                min_len = len(s)
                tar = s  
        for i in range(len(tar)):
            for s in strs:
                if s[i] != tar[i]:
                    return tar[:i]  
        return tar  