class Solution:
    def romanToInt(self, s: str) -> int:
        prev = None
        map = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        sm = 0
        for i in s[::-1]:
            if prev and map[prev]>map[i]:
                sm+=(-1*map[i])
            if prev and map[prev]<=map[i]:
                sm+=map[i]
            if not prev:
                sm+=map[i]
            prev = i
        return sm
                
            
        