from typing import List


def solution(board: List[List[int]]) -> int:
    if not board or not board[0]:
        return 0

    rows, cols = len(board), len(board[0])
    dp = [row[:] for row in board]
    max_side = 0

    for row in range(rows):
        for col in range(cols):
            if row == 0 or col == 0:
                max_side = max(max_side, dp[row][col])
                continue

            if dp[row][col] == 1:
                dp[row][col] = min(
                    dp[row - 1][col],
                    dp[row][col - 1],
                    dp[row - 1][col - 1],
                ) + 1
                max_side = max(max_side, dp[row][col])

    return max_side * max_side
