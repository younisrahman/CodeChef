for i in range(int(input())):
    a, b, c = map(int, input().split())
    if a > b and a > c:
        print("Alice")
    # elif a > b and a < c:
    #     print(c)
    elif b > a and b > c:
        print(b)
    # elif b > a and b < c:
    #     print(c)
    elif c > a and c > b:
        print(c)
    # elif c > a and c < b:
    #     print(b)
