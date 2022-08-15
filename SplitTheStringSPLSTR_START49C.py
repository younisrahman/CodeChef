import math
for i in range(int(input())):
    n, k = map(int, input().split())
    s = input()
    c0 = s.count('0')
    c1 = s.count('1')
    print(math.ceil(abs(c0-c1)/k))
