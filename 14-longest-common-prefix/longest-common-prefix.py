class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        m = min(strs)
        n =  max(strs)
        res = ""

        for i in range(len(m)):
            if m[i]!=n[i]:
                return res
            else:
                res+=m[i]
        return res
                
        