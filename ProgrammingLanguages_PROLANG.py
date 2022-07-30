for i in range(int(input())):
    arr = list(map(int, input().split()))
    one = 0
    two = 0
    if arr[0] == arr[2]:
        one += 1
    elif arr[0] == arr[3]:
        one += 1
    if arr[1] == arr[2]:
        one += 1
    elif arr[1] == arr[3]:
        one += 1

    if arr[0] == arr[4]:
        two += 1
    elif arr[0] == arr[5]:
        two += 1
    if arr[1] == arr[4]:
        two += 1
    elif arr[1] == arr[5]:
        two += 1

    if one == 2:
        print(1)
    elif two == 2:
        print(2)
    else:
        print(0)
