class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ele_idx_map = {}
        for i, j in enumerate(nums):
                t = target-j
                if t in ele_idx_map:
                    return [i,ele_idx_map[t]]
                else:
                    ele_idx_map[j]=i
        

                
        