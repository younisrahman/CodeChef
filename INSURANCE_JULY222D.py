for i in range(int(input())):
    x, y = map(int, input().split())
    if x < y:
        print(x)
    else:
        print(y)
