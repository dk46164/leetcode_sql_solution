class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        if numRows==1:
            return [[1]]
        elif numRows==2:
            return [[1],[1,1]]
        else:
            # intialized the results
            pascl_rows = [[1],[1,1]]

            # loop through each (n-2)
            for idx in range(numRows-2):
                prev_res = []
                prev_val = 0
                for val in pascl_rows[-1]:
                    prev_res.append(prev_val+val)
                    prev_val=val
                prev_res.append(1)
                pascl_rows.append(prev_res)
            return pascl_rows



        