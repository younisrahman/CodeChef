n = int(input())
count = 1
loop = False
for i in range(n):
    x, y, z = map(int, input().split())
    loop = True
    while loop:
        if (y*count) <= x:
            print(count*z)
            loop = False
        count += 1
