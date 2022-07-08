# Group Assignment

for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    dict = {}
    for j in a:
        if j in dict:
            dict[j] += 1
        else:
            dict[j] = 1
    list_keys = list(dict.keys())
    list_values = list(dict.values())
    count = 0
    for k in range(len(list_keys)):
        if list_values[k] % list_keys[k] != 0:
            print("NO")
            count += 1
            break
    if count == 0:
        print("YES")
