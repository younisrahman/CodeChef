for _ in range(int(input())):
    n = int(input())
    s = input()
    str = ''
    for i in range(0, n, 2):

        ns = f'{s[i]}{s[i+1]}'
        if ns == '00':
            str += 'A'
        elif ns == '11':
            str += 'G'
        elif ns == '10':
            str += 'C'
        elif ns == '01':
            str += 'T'
    print(str)
