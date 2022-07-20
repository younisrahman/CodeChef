for i in range(int(input())):
    x = int(input())
    z = input()
    if z == z[::-1]:
        print("YES")
    else:
        str = list(z)
        p = False
        for i in range(x-2):
            str[i], str[i+2] = str[i+2], str[i]
            if str == str[::-1]:
                p = True
                break
        if p:
            print("YES")
        else:
            print("NO")
