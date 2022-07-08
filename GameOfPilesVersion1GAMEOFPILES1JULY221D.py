
for i in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))[:n]
    s = 0
    c = 0
    for i in range(n):
        s += arr[i]
        if arr[i] == 1:
            c += 1
    if c > 0:
        print("CHEF")
    else:
        if s % 2 == 0:
            print("CHEFINA")
        else:
            print("CHEF")
