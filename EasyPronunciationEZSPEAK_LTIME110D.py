for i in range(int(input())):
    vowel = ['a', 'e', 'i', 'o', 'u']
    count = 0
    x = int(input())
    z = input()
    for i in z:
        if i not in vowel:
            count += 1
        else:
            count = 0
        if count == 4:
            break

    if count < 4:
        print('YES')
    else:
        print('NO')
