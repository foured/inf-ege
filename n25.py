# from fnmatch import *
#
# for i in range(0, 10**10, 98591):
#     if fnmatch(str(i), '5?2*3?3?'):
#         print(i, i // 98591)

# def get_A(n):
#     d = [1]
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             d.append(i)
#             d.append(n // i)
#     d = set(d)
#     return sum(d) // len(d)
#
# count = 0
# for N in range(770_000 - 1, 0, -1):
#     A = get_A(N)
#     if A % 100 == 12:
#         count += 1
#         print(N, A)
#         if count == 5:
#             break

# from fnmatch import *
# for i in range(0, 10 ** 10, 4173):
#     if fnmatch(str(i), '1?2655*8'):
#         print(i)

from fnmatch import *
for i in range(0, 10**10, 1917):
    if fnmatch(str(i), '3?12?14*5'):
        print(i, i//1917)