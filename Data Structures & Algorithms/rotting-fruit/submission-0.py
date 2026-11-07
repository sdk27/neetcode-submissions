class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        fresh = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    queue.append((row, col))
                elif grid[row][col] == 1:
                    fresh += 1

        minutes = 0

        while queue and fresh > 0:
            for _ in range(len(queue)):
                row, col = queue.popleft()

                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    next_row = row + dr
                    next_col = col + dc

                    if (0 <= next_row < rows
                        and 0 <= next_col < cols
                        and grid[next_row][next_col] == 1):
                        grid[next_row][next_col] = 2
                        fresh -= 1
                        queue.append((next_row, next_col))

            minutes += 1

        if fresh == 0:
            return minutes
        return -1
        