import heapq as hq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # create max heap
        nums_c = list(map(lambda k:-1*k,nums))
        hq.heapify(nums_c)

        #init reslt 
        k_ele = None

        # loop till k>0
        while k:
            k_ele = hq.heappop(nums_c)
            k-=1
        
        return -1*k_ele
        

        