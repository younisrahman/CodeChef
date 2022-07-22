for i in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    res = 0
    count = 0
    for i in range(n):
        if arr[i] == 1:
            count += 1
        else:
            res += count*(count+1)//2
            count = 0
    res += count*(count+1)//2
    print(res)
