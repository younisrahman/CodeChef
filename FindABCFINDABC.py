
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))[:n]
    aa = 0
    bb = 0
    cc = 0
    ok = False
    for a in range(n+1):
        for b in range(n+1):
            for c in range(n+1):
                for d in range(len(arr)):
                    if ((a ^ d) + (b ^ d) + (c ^ d)) == arr[d]:
                        ok = True
                    else:
                        ok = False
                        break
                if ok == True:
                    aa = a
                    bb = b
                    cc = c
                    break
            if ok == True:
                break
        if ok == True:
            break

    print(aa, bb, cc)
