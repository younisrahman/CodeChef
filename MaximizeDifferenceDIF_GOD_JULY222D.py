
for _ in range(int(input())):
    arr = list(map(int, input().split()))
    arr += [0, 0, 0, -1, arr[0], pow(2, 32)]
    while arr[-2] < arr[1]+1 and arr[-2] <= arr[-1]:
        arr[-4], arr[-5] = arr[-2], arr[1]//arr[-2]*arr[-2]
        arr[-1] = min(arr[-1], arr[-4]+(arr[1]-arr[-5]))
        if arr[-5]-arr[-4] > arr[-3]:
            arr[-3] = arr[-5]-arr[-4]
            arr[-6] = arr[-2]
        arr[-2] += 1
    print(arr[-6], arr[-6]+arr[-3])
