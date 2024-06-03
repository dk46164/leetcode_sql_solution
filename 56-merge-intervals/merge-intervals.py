class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        n = len(intervals) # size of the array

        # sort the given intervals:
        intervals.sort()

        ans = [intervals[0]]

        for idx in range(1,n):
            if ans[-1][-1]<intervals[idx][0]:
                ans.append(intervals[idx])
            else:
                ans[-1][-1] = max(ans[-1][-1],intervals[idx][1])
        
        return ans


            