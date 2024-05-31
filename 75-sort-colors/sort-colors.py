class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # intialize start and end index
        i_idx =0
        m_idx = 0
        l_idx = len(nums)-1

        # loop while i<j
        while m_idx<=l_idx:
            if not nums[m_idx]:
                # swap i and j elements
                nums[i_idx],nums[m_idx] = nums[m_idx],nums[i_idx]
                # increase pointer 
                i_idx+=1
                m_idx+=1
            elif nums[m_idx]==1:
                # increase ppinter
                m_idx+=1
            else:
                # swap i and j elements
                nums[l_idx],nums[m_idx] = nums[m_idx],nums[l_idx]
                # decrease pointer
                l_idx-=1



            



        