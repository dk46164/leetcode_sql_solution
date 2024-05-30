import math
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums)==1 : 
            return nums[0]
        else:
            max_s = -math.inf
            n = len(nums)
            i=0
            sum_s = 0
            st_idx = -1
            ed_idx = -1

            while i<n:
                sum_s+=nums[i]
                if sum_s>max_s:
                    max_s=sum_s
                if sum_s<0:
                    sum_s = 0
                i+=1
        return max_s
                

        