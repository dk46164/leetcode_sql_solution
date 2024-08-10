class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        # ind trunc idx
        k  = k if k>1  else 1
        trunc_idx = 0

        for idx in range(len(s)):
            if k==0:
                trunc_idx = idx
                break
            if s[idx].isspace():
                k-=1
        if k:
            return s
        else:
            return s[:trunc_idx-1]



        