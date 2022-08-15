t = int(input())
for i in range(t):
    n, x, y = map(int, input().split())
    if x+(y*2) <= n:
        print("YES")
    else:
        print("NO")
