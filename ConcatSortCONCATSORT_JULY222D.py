for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    count = 0
    arr2 = sorted(arr)
    p = []
    q = []
    for i in range(n):
        if i == 0:
            p.append(arr2[i])
            continue
        if arr.index(arr2[i]) > arr.index(arr2[i-1]) and len(q) == 0:
            p.append(arr2[i])
        elif len(q) == 0 or arr.index(arr2[i]) > arr.index(q[-1]):
            q.append(arr2[i])

    print("YES" if (len(p) + len(q)) == len(arr) else "NO")
    # print(p, q)
