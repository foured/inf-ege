# count = 0
# alf = 'ШКОЛА'
# w = product(alf, repeat=3)
# for i in w:
#     word = ''.join(i)
#     if word.count('К') == 1:
#         count += 1
# print(count)

# count = 0
# products = product('012345678', repeat=5)
# for p in products:
#     n = ''.join(p)
#
#     if n[0] != '0' and n.count('5') == 1:
#         f = True
#         for j in range(0, len(n) - 1):
#             if n[j] == n[j + 1]:
#                 f = False
#                 break
#         if f:
#             count += 1
#
# print(count)

# count = 0
# products = product('0123456789ABCDE', repeat=5)
# for i in products:
#     p = ''.join(i)
#     if p[0] != '0' and p.count('8') == 1:
#         k = 0
#         for c in p:
#             if int(c, 15) > 9:
#                 k += 1
#         if k >= 2:
#             count += 1
# print(count)

# count = 0
# products = product('КОСУФ', repeat=5)
#
# for i in products:
#     p = ''.join(i)
#     count += 1
#     if (p.count('Ф') == 0 and p.count('У') == 2):
#         print(count)

# count = 0
# products = product('01234567', repeat=5)
# for i in products:
#     p = ''.join(i)
#     if p[0] not in '01357' and p[-1] not in '26' and p.count('7') <= 2:
#         count += 1
# print(count)

# from itertools import product
#
# count = 0
# products = product('0123456789AB', repeat=5)
# for i in products:
#     p = ''.join(i)
#
#     if p.count('7') == 1 and p[0] != '0' and (p.count('9') + p.count('A') + p.count('B')) <= 3:
#         count += 1
# print(count)

# from itertools import *
#
# ps = product('ЕКМОПРТЬЮ', repeat=5)
# n = 0
# for i in ps:
#     n += 1
#     p = ''.join(i)
#     if n % 2 == 1 and p[0] != 'Ь' and p.count('К') == 2:
#         print(n, p)

from itertools import *
a = sorted(set('ПАВСИКАКИЙ'))
p = product(a, repeat=6)

c = 0
for i in p:
    w = ''.join(i)
    if 'АИ' in w or 'ИА' in w or 'АА' in w or 'ИИ' in w:
        c += 1
        if w == 'КАКААА':
            print(c)
            break