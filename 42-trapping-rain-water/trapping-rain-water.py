class Solution:
    def trap(self, height: List[int]) -> int:

        # init vars
        lft = 0
        rgt = len(height)-1
        lft_max = height[lft]
        rgt_max = height[rgt]
        tot_wt = 0

        # loop through
        while lft<rgt:
            if lft_max<=rgt_max:
                tot_wt+=(lft_max-height[lft])
                lft+=1
                lft_max = max(lft_max,height[lft])
            else:
                tot_wt+=(rgt_max-height[rgt])
                rgt-=1
                rgt_max = max(rgt_max,height[rgt])
        return tot_wt
        