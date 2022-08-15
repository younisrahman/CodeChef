n = int(input())
for i in range(n):
    x, y, z = map(int, input().split())
    if x <= y:
        print(z)
    else:
        loop = True
        count = 1
        while loop:
            if (y*count) >= x:
                print(count*z)
                loop = False
            count += 1
