class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = defaultdict(lambda :-1)
        stack  = []
        for i in range(len(nums2)):
            while stack and stack[-1]<nums2[i]:
                res[stack.pop()] = nums2[i]
            stack.append(nums2[i])
        for i in range(len(nums1)):
            nums1[i] = res[nums1[i]]
        
        return nums1

        