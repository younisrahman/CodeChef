
for i in range(int(input())):
    # for j in range(int(input())):
    n = int(input())
    x = list(map(int, input().split()))
    x = sorted(x)
    turn = 'CHEF'
    if x[0] == 1:
        print("CHEF")
    elif len(x) == 1:
        if x[0] % 2 == 0:
            print("CHEFINA")
        else:
            print("CHEF")
    else:
        for k in range(n):
            print('k', k)
            for l in range(x[k]-1):
                print('l', l)
                if turn == 'CHEF':
                    turn = 'CHEFINA'
                else:
                    turn = 'CHEF'

        if turn == 'CHEF':
            print('CHEFINA')
        else:
            print('CHEF')
