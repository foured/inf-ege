#2
# print('x y w z')
# for x in 0, 1:
#     for y in 0, 1:
#         for w in 0, 1:
#             for z in 0, 1:
#                 f = (y <= x) and (not w) and z
#                 if f == 1:
#                     print(x, y, w, z)
import itertools
#5
# m = 10000
# for n in range(1, 100):
#     bn = bin(n)[2::]
#     if bn.count('1') % 2 == 0:
#         bn += '11'
#     else:
#         bn += '01'
#     r = int(bn, 2)
#     if r > 61:
#         m = min(m, r)
# print(m)

#8
from itertools import *

# products = itertools.product('БЕНРСТЬЯ', repeat = 5)
# count = 0
# res = -1
# for p in products:
#     w = ''.join(p)
#     count += 1
#     print(w)
#     if count % 2 == 0 and w[0] == 'Р' and w.count('Ь') == 0:
#         res = count
#     elif res != -1 and w[0] != 'Р':
#         print(res)
#         break

#9
# file = open(r"D:\Python\informatics\n9_12_10.txt")
# count = 0
# for line in file:
#     arr = [int(x) for x in line.split()]
#     arr.sort()
#     max1 = arr[-1]
#     max2 = arr[-2]
#     arrnm = arr[:-2]
#     o5 = [x for x in arr if str(x)[-1] == '5']
#     if (max1 + max2) * 2 > sum(arrnm) * 3 and len(o5) >= 2:
#         count += 1
# print(count)

#12
# l = '9' * 68
# while '22222' in l or '9999' in l:
#     if '22222' in l:
#         l = l.replace('22222', '99', 1)
#     else:
#         l = l.replace('9999', '29', 1)
# print(l)

#13
# from ipaddress import *
# net = ip_network('228.172.236.0/255.255.240.0', False)
# count = 0
# for ip in net:
#     if f'{ip:b}'.count('1') % 5 != 0:
#         count += 1
# print(count)

def to_sys(num, osn):
    alf = '0123456789ABCDEF'
    res = ''
    while num > 0:
        res = alf[num % osn] + res
        num //= osn
    return res

#14
# n = 4**644 + 4**322 + 16**35 - 64**3
# n4 = to_sys(n, 4)
# print(n4.count('3'))

#15
# def f(x, y, a):
#     return (x <= 19) or (y < (2 * x + a - 50)) or (y > 17)
#
# for a in range(1, 100):
#     if all(f(x, y, a) for x in range(1, 100) for y in range(1, 100)):
#         print(a)
#         break

#16
# def f(n):
#     if n > 400:
#         return n**n
#     return n + 6 + f(n + 12)
#
# print(f(72) - f(108))

#17
# file = open(r"C:\Users\Ivan\Downloads\17_17750.txt")
# count = 0
# ms = -1
# arr = [int(x) for x in file]
# for i in range(0, len(arr) - 1):
#     n1 = arr[i]
#     n2 = arr[i + 1]
#     if ((n1 % 77) + (n2 % 77)) == min(arr):
#         count += 1
#         ms = max(n1 + n2, ms)
# print(count)
# print(ms)

#19-21
# def f(s, t, c):
#     if s >= 54:
#         return t % 2 == c % 2
#
#     if t >= c:
#         return 0
#
#     h = [f(s + 2, t + 1, c), f(s * 2, t + 1, c)]
#     return any(h) if (t + 1) % 2 == c % 2 else all(h)
#
# print('19: ', [s for s in range(1, 435) if f(s, 0, 1) == 0 and f(s, 0, 2)])
# print('20: ', [s for s in range(1, 435) if f(s, 0, 1) == 0 and f(s, 0, 3)])
# print('20: ', [s for s in range(1, 435) if f(s, 0, 2) == 0 and f(s, 0, 4)])

#23
# def d(f, t):
#     if f == t:
#         return 1
#     if f > t:
#         return 0
#     if f == 22:
#         return 0
#     return d(f + 3, t) + d(f + 4, t)
#
# print(d(16,38))

#24
# f = open(r"C:\Users\Ivan\Downloads\24_17756.txt")
# s = f.read().replace('++', '+;+').replace('**', '*;*').replace('*+', '*;+').replace('+*', '+;*')
# s = s.replace('++', '+;+').replace('**', '*;*').replace('*+', '*;+').replace('+*', '+;*')
# print(max([len(x) for x in s.split(';')]))

#25
from fnmatch import *

for i in range(0, 10**10, 2025):
    if fnmatch(str(i), '21?3*145?5'):
        print(i, i // 2025)
