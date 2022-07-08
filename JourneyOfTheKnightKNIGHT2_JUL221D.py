# def knight(x, y, x2, y2, max, total):
#     # print(total)
#     if total == 100:
#         return (x, y, total)
#     if x == x2 and y == y2:
#         return (x, y, total)

#     if x+1 <= max and y+2 <= max:
#         return knight(x+1, y+2, x2, y2, max, total+1)
#     elif x+2 <= max and y+1 <= max:
#         return knight(x+2, y+1, x2, y2, max, total+1)
#     elif x-1 >= 0 and y+2 <= max:
#         return knight(x-1, y+2, x2, y2, max, total+1)
#     elif x-2 >= 0 and y+1 <= max:
#         return knight(x-2, y+1, x2, y2, max, total+1)
#     elif x-2 >= 0 and y-1 >= 0:
#         return knight(x-2, y-1, x2, y2, max, total+1)
#     elif x-1 >= 0 and y-2 >= 0:
#         return knight(x-1, y-2, x2, y2, max, total+1)
#     elif x+1 <= max and y-2 >= 0:
#         return knight(x+1, y-2, x2, y2, max, total+1)
#     elif x+2 <= max and y-1 >= 0:
#         return knight(x+2, y-1, x2, y2, max, total+1)
#     # else:
#     #     return (x, y, total)


for i in range(int(input())):
    max = 8
    total = 0
    x, y, x2, y2 = map(int, input().split())
    # print(knight(x, y, x2, y2, max, total))
    while total <= 100:
        print(total)
        if x == x2 and y == y2:
            print(x, y, total)
            break
        if x+1 <= max and y+2 <= max:
            x = x+1
            y = y+2
            total = total+1
        elif x+2 <= max and y+1 <= max:
            x = x+2
            y = y+1
            total = total+1
        elif x-1 >= 0 and y+2 <= max:
            x = x-1
            y = y+2
            total = total+1
        elif x-2 >= 0 and y+1 <= max:
            x = x-2
            y = y+1
            total = total+1
        elif x-2 >= 0 and y-1 >= 0:
            x = x-2
            y = y-1
            total = total+1
        elif x-1 >= 0 and y-2 >= 0:
            x = x-1
            y = y-2
            total = total+1
        elif x+1 <= max and y-2 >= 0:
            x = x+1
            y = y-2
            total = total+1
        elif x+2 <= max and y-1 >= 0:
            x = x+2
            y = y-1
            total = total+1
        else:
            total+1
    print(x, y, total)
