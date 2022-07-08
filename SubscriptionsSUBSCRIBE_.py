for i in range(int(input())):
    n, x = map(int, input().split())
    if n % 6 == 0:
        print((n//6)*x)
    else:
        print(((n//6)+1)*x)
