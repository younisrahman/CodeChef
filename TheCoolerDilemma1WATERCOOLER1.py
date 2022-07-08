for i in range(int(input())):
    x, y, m = map(int, input().split())
    if (x*m) < y:
        print("YES")
    else:
        print("NO")
