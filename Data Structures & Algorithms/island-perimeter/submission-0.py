class Solution:

    def islandPerimeter(self, grid):

        rows = len(grid)
        cols = len(grid[0])

        perimeter = 0

        # Shashank pura island check kar raha hai
        for r in range(rows):

            for c in range(cols):

                # agar land mila
                if grid[r][c] == 1:

                    # initially 4 sides maan lo
                    perimeter += 4

                    # upar bhi land hai
                    # toh ek side gayi
                    if r > 0 and grid[r - 1][c] == 1:
                        perimeter -= 1

                    # neeche bhi land hai
                    if r < rows - 1 and grid[r + 1][c] == 1:
                        perimeter -= 1

                    # left me bhi land hai
                    if c > 0 and grid[r][c - 1] == 1:
                        perimeter -= 1

                    # right me bhi land hai
                    if c < cols - 1 and grid[r][c + 1] == 1:
                        perimeter -= 1

        return perimeter