class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:

        # Use a 64-bit integer to cover the entire range (1 to 50)
        coverage = 0
        
        for start, end in ranges:
            # Set bits for all numbers in the range
            coverage |= ((1 << (end - start + 1)) - 1) << (start - 1)
        
        # Create a mask for the target range
        target = ((1 << (right - left + 1)) - 1) << (left - 1)
        
        # Check if all numbers from left to right are covered
        return (coverage & target) == target
        