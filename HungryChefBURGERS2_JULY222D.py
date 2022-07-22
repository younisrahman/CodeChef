for i in (range(int(input()))):
    normal, premium, need, money = map(int, input().split())
    if money // normal < need:
        print('-1')
    else:
        nor = need
        prem = 0
        mney = money - (need * normal)
        while mney >= 0:
            mney -= (premium-normal)
            if mney < 0:
                break
            prem += 1
            nor -= 1
            if nor == 0:
                break
        print(nor, prem)
