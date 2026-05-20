from typing import List

class Solution:

    def countServers(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])

        # count servers in every row
        rowCount = [0] * rows

        # count servers in every column
        colCount = [0] * cols

        # first pass
        # store row and column counts
        for r in range(rows):

            for c in range(cols):

                if grid[r][c] == 1:

                    rowCount[r] += 1
                    colCount[c] += 1

        ans = 0

        # second pass
        # check communication
        for r in range(rows):

            for c in range(cols):

                if grid[r][c] == 1:

                    # same row or same column
                    # should contain another server
                    if rowCount[r] > 1 or colCount[c] > 1:

                        ans += 1

        return ans