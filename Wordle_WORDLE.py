for i in range(int(input())):
    a = input()
    b = input()
    str = ''
    for i in range(len(a)):
        if a[i] == b[i]:
            str += 'G'
        else:
            str += 'B'
    print(str)
