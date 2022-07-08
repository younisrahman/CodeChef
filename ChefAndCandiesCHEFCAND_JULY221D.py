for i in range(int(input())):
    a, b = map(int, input().split())
    if b > a:
        print(0)
    else:
        if (a-b) % 4 == 0:
            print((a-b)//4)
        else:
            print(((a-b)//4) + 1)
