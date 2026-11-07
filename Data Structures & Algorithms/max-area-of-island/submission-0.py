class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        largest_area = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    area = 0
                    stack = [(row, col)]
                    grid[row][col] = 0

                    while stack:
                        current_row, current_col = stack.pop()
                        area += 1

                        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                            next_row = current_row + dr
                            next_col = current_col + dc

                            if (0 <= next_row < rows
                                and 0 <= next_col < cols
                                and grid[next_row][next_col] == 1):
                                grid[next_row][next_col] = 0
                                stack.append((next_row, next_col))

                    largest_area = max(largest_area, area)

        return largest_area
        