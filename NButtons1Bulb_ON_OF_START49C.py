for i in range(int(input())):
    n = int(input())
    s = input()
    r = input()
    state = True
    for j in range(n):
        if s[j] != r[j]:
            state = not state
    print(1 if state else 0)
