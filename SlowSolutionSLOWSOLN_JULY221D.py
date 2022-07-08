for i in range(int(input())):
    a, b, c = map(int, input().split())
    new = []
    for i in range(a):
        if c < b:
            new.append(c)
        else:
            new.append(b)
        c = c - b
        if c <= 0:
            break
    # for i in

    print(new)
