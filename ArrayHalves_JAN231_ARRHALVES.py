for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    swap, j = 0, 0
    for i in range(2*n):
        if arr[i] <= n:
            swap += (i-j)
            j += 1
    print(swap)
