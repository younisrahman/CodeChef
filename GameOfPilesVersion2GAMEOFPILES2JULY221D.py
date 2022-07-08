turn = 'CHEF'
for i in range(int(input())):
    # for j in range(int(input())):
    n = int(input())
    x = list(map(int, input().split()))
    s = sum(x)
    # if s == 0:
    #     if turn == 'CHEF':
    #         turn = 'CHEFINA'
    #         print('CHEF')
    #     else:
    #         turn = 'CHEF'
    #         print('CHEFINA')
    # elif s == 1:
    #     if turn == 'CHEF':
    #         turn = 'CHEFINA'
    #         print('CHEF')
    #     else:
    #         turn = 'CHEF'
    #         print('CHEFINA')
    # else:
    if s % 2 == 0:
        if turn == 'CHEF':
            turn = 'CHEFINA'
            print('CHEF')
        else:
            turn = 'CHEF'
            print('CHEFINA')
    else:
        if turn == 'CHEF':
            turn = 'CHEFINA'
            print('CHEF')
        else:
            turn = 'CHEF'
            print('CHEFINA')
    # if s % 2 == 0:
    #     if turn == 0:
    #         print("CHEF")
    #     else:
    #         print("CHEFINA")

    # else:
    #     if turn == 0:
    #         print("CHEF")
    #     else:
    #         print("CHEFINA")
