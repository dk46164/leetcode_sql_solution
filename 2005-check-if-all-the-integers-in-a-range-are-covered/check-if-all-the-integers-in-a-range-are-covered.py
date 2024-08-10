class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:

        # inti bit set
        range_bit =[False]*50
        left-=1
        right-=1

        for ele in ranges:
            range_bit[ele[0]-1:ele[1]] = [True]*(ele[1]-ele[0]+1)

        print(range_bit)
        if left==right:
            return range_bit[left%50] 
        else:
            return all(range_bit[left:right+1])

        