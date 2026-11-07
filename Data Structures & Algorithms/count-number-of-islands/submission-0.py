class Solution:
     def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        islands = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    islands += 1
                    stack = [(row, col)]
                    grid[row][col] = "0"

                    while stack:
                        current_row, current_col = stack.pop()

                        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                            next_row = current_row + dr
                            next_col = current_col + dc

                            if (0 <= next_row < rows
                                and 0 <= next_col < cols
                                and grid[next_row][next_col] == "1"):
                                grid[next_row][next_col] = "0"
                                stack.append((next_row, next_col))

        return islands