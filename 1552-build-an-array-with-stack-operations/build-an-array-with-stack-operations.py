class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:

        # result set
        stack = []

        # tmp result set
        tmp = list(range(1,max(target)+1))

        # loop through stream and get result
        while tmp:
            if tmp[0] in target:
                stack.append('Push')
                tmp.pop(0)
            else:
                stack.append('Push')
                stack.append('Pop')
                tmp.pop(0)
        return stack

        