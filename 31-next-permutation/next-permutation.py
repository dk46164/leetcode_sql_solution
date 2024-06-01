class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        b_idx =-1

        if n==2:
            nums[0],nums[1]=nums[1],nums[0]
            return
        if n==1:
            return 

        # find dip index
        for i in range(n-2,-1,-1):
            if nums[i]<nums[i+1]:
                b_idx=i
                break

        # if dip index is not none(swap, b_idx, just greater elements)
        if b_idx>=0:
            for i in range(n-1,b_idx,-1):
                if nums[i]>nums[b_idx]:
                    nums[i],nums[b_idx]=nums[b_idx],nums[i]
                    break
            # sort b_idx to end 
            nums[b_idx+1:] = sorted(nums[b_idx+1:])
        else:
            nums.sort()


        

        



        