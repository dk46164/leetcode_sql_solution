class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr_cnt = 0
        prev_cnt = 0
        for val in nums:
            if val:
                curr_cnt+=1
            else:
                prev_cnt = max(curr_cnt,prev_cnt)
                curr_cnt = 0
        
        return max(prev_cnt,curr_cnt)
        