class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return

        rows = len(board)
        cols = len(board[0])
        stack = []

        def add_if_border_o(row, col):
            if board[row][col] == "O":
                board[row][col] = "S"
                stack.append((row, col))

        for row in range(rows):
            add_if_border_o(row, 0)
            add_if_border_o(row, cols - 1)

        for col in range(cols):
            add_if_border_o(0, col)
            add_if_border_o(rows - 1, col)

        while stack:
            row, col = stack.pop()

            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                next_row = row + dr
                next_col = col + dc

                if (0 <= next_row < rows
                    and 0 <= next_col < cols
                    and board[next_row][next_col] == "O"):
                    board[next_row][next_col] = "S"
                    stack.append((next_row, next_col))

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "O":
                    board[row][col] = "X"
                elif board[row][col] == "S":
                    board[row][col] = "O"