n = int(input())
for i in range(n):
    x, y, a = map(int, input().split())
    if a >= x and a < y:
        print("YES")
    else:
        print("NO")
