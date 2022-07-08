turn = 'CHEF'
for i in range(int(input())):
    # for j in range(int(input())):
    n = int(input())
    x = list(map(int, input().split()))
    s = sum(x)
    if s % 2 == 0:
        print("CHEFINA")
    else:
        print("CHEF")

    # if s % 2 == 0:
    #     if turn == 'CHEF':
    #         turn = 'CHEFINA'
    #         print('CHEF')
    #     else:
    #         turn = 'CHEF'
    #         print('CHEFINA')
    # else:
    #     if turn == 'CHEF':
    #         turn = 'CHEFINA'
    #         print('CHEF')
    #     else:
    #         turn = 'CHEF'
    #         print('CHEFINA')
