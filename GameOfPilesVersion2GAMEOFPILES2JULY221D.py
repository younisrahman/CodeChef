# for _ in range(int(input())):
#     n = int(input())
#     arr = list(map(int, input().split()))[:n]
#     s = 0
#     c = 0
#     turn = 'CHEF'
#     for i in range(n):
#         if arr[i] > 1:
#             s += arr[i]-1
#         else:
#             s += arr[i]
#         if arr[i] == 1:
#             c += 1
#         if turn == 'CHEF':
#             turn = 'CHEFINA'
#         else:
#             turn = 'CHEF'
#         # if (i+3) == n:
#         #     break
#     if c > 0:
#         if c % 2 == 0:
#             print("CHEFINA")
#         else:
#             print("CHEF")
#     else:
#         if s % 2 == 0:
#             if turn == 'CHEF':
#                 print("CHEFINA")
#             else:
#                 print("CHEF")
#         else:
#             if turn == 'CHEF':
#                 print("CHEF")
#             else:
#                 print("CHEFINA")
#     print(1 % 2)


for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))[:n]
    s = 0
    c = 0
    cp = 0
    turn = 'CHEF'
    for i in range(n):
        if arr[i] > 1:
            if (arr[i]-1) % 2 == 0:
                if turn == 'CHEF':
                    turn = 'CHEFINA'
                else:
                    turn = 'CHEF'
            else:
                if turn == 'CHEF':
                    turn = 'CHEF'
                else:
                    turn = 'CHEFINA'
            c += 1
        else:
            if turn == 'CHEF':
                turn = 'CHEFINA'
            else:
                turn = 'CHEF'
            cp += 1
    if cp > 0:
        if cp % 2 == 0:
            print("CHEFINA")
        else:
            print("CHEF")
    else:
        if turn == 'CHEF':
            print('CHEFINA')
        else:
            print('CHEF')
