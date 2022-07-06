n = int(input())
count = 0
loop = False
for i in range(n):
    num = int(input())
    if num % 3 == 0:
        print(0)
    else:
        loop = True
        count = 1
        while loop:
            if (num+count) % 3 == 0:
                print(count)
                loop = False
            count += 1
