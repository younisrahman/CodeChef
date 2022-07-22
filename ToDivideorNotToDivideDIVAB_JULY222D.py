# # ToDivideorNotToDivideDIVAB_JULY222D
# for i in (range(int(input()))):
#     a, b, n = map(int, input().split())
#     if a % b == 0:
#         print('-1')
#     else:
#         if (((n//a)+1)*a) % b == 0:
#             print(((n//a)+2)*a)
#         else:
#             print(((n//a)+1)*a)


def ans(a, b, n):
    if a % b == 0:
        return -1
    x = n
    if x % a != 0:
        x = n+a-(x % a)
    while not (x % a == 0 and x % b != 0):
        x += a
    return x


for i in (range(int(input()))):
    a, b, n = map(int, input().split())
    print(ans(a, b, n))
