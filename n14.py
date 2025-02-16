def to_sys(num, osn):
    alf = '0123456789ABCDEF'
    res = ''
    while num > 0:
        res = alf[num % osn] + res
        num //= osn
    return res

# m = 0
# for x in range(0, 2031):
#     c = 7**170 + 7**100 - x
#     if to_sys(c, 7).count('0') == 71:
#         m = max(m, x)
# print(m)

# c = 3 * 3125**8 + 2 * 625**7 - 4 * 625**6 + 3 * 125**5 - 2 * 25**4 - 2025
# count = 0
# while c > 0:
#     if c % 25 == 0:
#         count += 1
#     c //= 25
# print(count)

# 98897x21 + 2x923

# for x in range(0, 19):
#     s1 = 1 * 19**0 + 2 * 19**1 + x * 19**2 + 7 * 19**3 + 9 * 19**4 + 8 * 19**5 + 8 * 19**6 + 9 * 19**7
#     s2 = 3 * 19**0 + 2 * 19**1 + 9 * 19**2 + x * 19**3 + 2 * 19**4
#     if (s1 + s2) % 18 == 0:
#         print((s1 + s2) // 18)

# for x in range(0, 2031):
#     c = 6**260 + 6**160 + 6**60 - x
#     nc = 0
#     while c > 0:
#         if c % 6 == 0:
#             nc += 1
#         c //= 6
#     if nc == 202:
#         print(x)
#         break

# for x in range(0, 27):
#     s1 = 4 * 27**0 + 2 * 27**1 + x * 27**2 + 3 * 27**3 + 2 * 27**4 + 1 * 27**5
#     s2 = 8 * 27**0 + 7 * 27**1 + x * 27**2 + 5 * 27**3 + 3 * 27**4 + 1 * 27**5
#
#     if (s1 + s2) % 26 == 0:
#         print((s1 + s2) // 26)

# for x in range(1, 150):
#     n1 = 9 * 150**0 + 2 * 150**1 + x * 150**2 + 1 * 150**3 + 5 * 150**4
#     n2 = 3 * 150**0 + 2 * 150**1 + 0 * 150**2 + x * 150**3
#     s = n1 + n2
#     if s % 149 == 0:
#         print(s // 149, x)

# for x in range(1, 100):
#     n = 7**666 + 7**333 + 49**x - 343
#     c = 0
#     while n > 0:
#         if n % 7 == 6:
#             c += 1
#         n //= 7
#     if c == 49:
#         print(x)

m4 = 0
res = -1
a = 5**2025 + 5**400
for x in range(10, 70_001):
    n = a - x
    n4 = 0
    while n > 0:
        if n % 5 == 4:
            n4 += 1
        n //= 5
    if n4 >= m4:
        m4 = n4
        res = x
print(res)