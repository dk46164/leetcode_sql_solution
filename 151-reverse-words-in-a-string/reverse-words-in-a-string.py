class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(list(filter(lambda k:bool(k.strip())==True, s.split(' ') ))[::-1])
        