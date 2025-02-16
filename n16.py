# from functools import lru_cache
#
# @lru_cache(maxsize=None)
# def f(n):
#     if n < 3:
#         return 2
#     if n % 2 == 0:
#         return 2 * f(n - 2) - f(n - 1) + 2
#     return 2 * f(n - 1) + f(n - 2) - 2
# print(f(170))

# f = [2] * 171
# for n in range(3, len(f)):
#     if n % 2 == 0:
#         f[n] = 2 * f[n - 2] - f[n - 1] + 2
#     else:
#         f[n] = 2 * f[n - 1] + f[n - 2] - 2
#
# print(f[170])

import sys
sys.setrecursionlimit(10**8)

def f(n):
    if n > 3000:
        return n
    return (2 * n + 4) * f(n + 2)

print(sum([int(x) for x in str(f(20) // f(28))]))