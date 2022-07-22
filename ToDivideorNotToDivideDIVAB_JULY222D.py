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

# # ToDivideorNotToDivideDIVAB_JULY222D
# for i in (range(int(input()))):
#     a, b, n = map(int, input().split())
#     if a % b == 0:
#         print('-1')
#     else:
#         x = n
#         if not(x % a == 0):
#             x = (n+a)-(x % a)
#         else:
#             while not ((x % a == 0) and not(x % b == 0)):
#                 x += a
#         print(x)


# for i in (range(int(input()))):
#     a, b, n = map(int, input().split())
#     if a % b == 0:
#         print('-1')
#     else:
#         x = n
#         if not(x % a == 0):
#             x = (n+a)-(x % a)
#         else:
#             while not ((x % a == 0) and not(x % b == 0)):
#                 x += a
#         print(x)
