for i in range(int(input())):
    x, y, z = map(int, input().split())
    if x == y and y == z:
        print("YES")
    elif x == y:
        if z > y:
            print("YES")
        else:
            print("NO")
    elif y == z:

        if x > y:
            print("YES")
        else:
            print("NO")
    elif x == z:
        if y > z:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
