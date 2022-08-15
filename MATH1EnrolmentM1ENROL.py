for i in range(int(input())):
    x, y = map(int, input().split())
    if x < y:
        print(y-x)
    else:
        print(0)
