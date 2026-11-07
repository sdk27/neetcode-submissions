class Solution:
   def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        empty = 2147483647
        queue = deque()

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    queue.append((row, col))

        while queue:
            row, col = queue.popleft()

            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                next_row = row + dr
                next_col = col + dc

                if (0 <= next_row < rows
                    and 0 <= next_col < cols
                    and grid[next_row][next_col] == empty):
                    grid[next_row][next_col] = grid[row][col] + 1
                    queue.append((next_row, next_col))