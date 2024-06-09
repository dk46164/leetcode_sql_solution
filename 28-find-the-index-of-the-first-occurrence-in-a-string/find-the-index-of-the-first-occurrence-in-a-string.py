class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        # get len of str
        h_len = len(haystack)
        n_len = len(needle)
        for i in range(h_len):
            if needle==haystack[i:i+n_len]:
                return i
        return -1

        