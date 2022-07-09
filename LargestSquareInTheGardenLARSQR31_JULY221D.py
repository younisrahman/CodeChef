
n = int(input())
garden = [[0 for x in range(n)] for y in range(n)]

for i in range(n):
    a, b = map(int, input().split())
    for j in range(a, (b+1)):
        garden[i][j] = 1
cache = garden
result = 0
for i in range(n):
    for j in range(n):
        if i == 0 or j == 0:
            continue
        elif garden[i][j] > 0:
            cache[i][j] = 1+min(cache[i-1][j], cache[i][j-1], cache[i-1][j-1])

        if cache[i][j] > result:
            result = cache[i][j]

print(result)
