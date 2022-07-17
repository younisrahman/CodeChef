# # https: // www.youtube.com/watch?v = FO7VXDfS8Gk
# def maximum_square(matrix):
#     cache = matrix
#     result = 0
#     for i in range(n):
#         for j in range(n):
#             if i == 0 or j == 0:
#                 continue
#             elif matrix[i][j] > 0:
#                 cache[i][j] = 1+min(cache[i-1][j], cache[i]
#                                     [j-1], cache[i-1][j-1])

#             if cache[i][j] > result:
#                 result = cache[i][j]
#     return result


# n = int(input())
# garden = [[0]*n for _ in range(n)]

# for i in range(n):
#     a, b = map(int, input().split())
#     for j in range(a, (b+1)):
#         garden[i][j] = 1

# print(maximum_square(garden))

from itertools import product
tcs = 1
modd = int(1e9 + 7)


def dfs(dp):
    m, n, ans = len(dp), len(dp[0]), 0
    for i, j in product(range(m-1, -1, -1), range(n-1, -1, -1)):
        if i == m-1 or j == n-1:
            dp[i][j] = int(dp[i][j])
            ans = max(ans, dp[i][j])

        else:
            dp[i][j] = 1 + min(dp[i+1][j], dp[i][j+1], dp[i+1]
                               [j+1]) if dp[i][j] == 1 else 0
            ans = max(ans, dp[i][j])
    return ans


for tc in range(tcs):
    n = int(input())
    grid = [[0] * n for _ in range(n)]
    for r in range(n):
        a, b = map(int, input().split())
        b += 1
        for c in range(a, b):
            grid[r][c] = 1

    # print("grid, sep= "\n")

    ans = dfs(grid)
    print(ans)
