class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        rows = [[1], [1, 1]]
        if numRows <= 2:
            return rows[:numRows]
        for i in range(3, numRows+1):
            new_row = [x[0]+x[1] for x in itertools.pairwise(rows[-1])]
            new_row.insert(0,1)
            new_row.append(1)
            rows.append(new_row)
        return rows



        