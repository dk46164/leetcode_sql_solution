class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:

        # init variables
        high,low=len(nums)-2,1

        # edge case
        if high==-1:
            return nums[0]
        if nums[0]!=nums[1]:
            return nums[0]
        if nums[-1]!=nums[-2]:
            return nums[-1]
            
        while low<=high:
            mid  = (high+low)//2

            if nums[mid] != nums[mid + 1] and nums[mid] != nums[mid - 1]:
                return nums[mid]

            if (mid % 2 == 1 and nums[mid] == nums[mid - 1]) or (mid % 2 == 0 and nums[mid] == nums[mid + 1]):
                # Eliminate the left half:
                low = mid + 1

            else:
                # Eliminate the right half:
                high = mid - 1
        return -1