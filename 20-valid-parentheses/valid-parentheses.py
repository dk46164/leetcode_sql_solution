class Solution:
    def isValid(self, s: str) -> bool:
        hmap = {'(':')','{':'}','[':']'}
        stack = []
        i = 0
        while i<len(s):
            if s[i] in hmap:
                stack.append(s[i])
            else:
                if stack and hmap[stack[-1]]==s[i]:
                    stack.pop(-1)
                else:
                    return False
            i+=1
        return len(stack)==0
                
        