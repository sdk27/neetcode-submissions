from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])

        def reachable_from(starts):
            visited = set(starts)
            stack = list(starts)

            while stack:
                row, col = stack.pop()

                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    next_row = row + dr
                    next_col = col + dc

                    if (0 <= next_row < rows
                        and 0 <= next_col < cols
                        and (next_row, next_col) not in visited
                        and heights[next_row][next_col] >= heights[row][col]):
                        visited.add((next_row, next_col))
                        stack.append((next_row, next_col))

            return visited

        pacific_edges = (
            [(0, col) for col in range(cols)] +
            [(row, 0) for row in range(rows)]
        )
        atlantic_edges = (
            [(rows - 1, col) for col in range(cols)] +
            [(row, cols - 1) for row in range(rows)]
        )

        pacific = reachable_from(pacific_edges)
        atlantic = reachable_from(atlantic_edges)

        return [
            [row, col]
            for row in range(rows)
            for col in range(cols)
            if (row, col) in pacific and (row, col) in atlantic
        ]