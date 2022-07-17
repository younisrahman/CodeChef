for i in range(int(input())):
    x, y, z = map(int, input().split())
    btime = 0
    if x % 3 == 0:
        btime = ((x//3) - 1)*z
    else:
        btime = (x//3)*z
    print((x*y)+btime)
