for i in range(int(input())):
    # for j in range(int(input())):
    n = int(input())
    x = list(map(int, input().split()))
    chef = 0
    chefina = 0
    for k in range(n):
        if k == 0:
            chef = x[k]
        elif k == 1:
            chefina = x[k]
        else:
            if k % 2 == 0:
                chef += x[k]
            else:
                chefina += x[k]

    print("CHEF" if chef < chefina else "CHEFINA")
