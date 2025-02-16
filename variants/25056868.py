#2
# print('x y w z')
# for x in 0, 1:
#     for y in 0, 1:
#         for w in 0, 1:
#             for z in 0, 1:
#                 f = (not(x <= w)) or (y <= z) or (not y)
#                 if f == 0:
#                     print(x, y, w, z)

def to_sys(n, osn):
    alf = '0123456789ABCDEF'
    res = ''
    while n > 0:
        res = alf[n % osn] + res
        n //= osn
    return res

#5
# for n in range(1, 100):
#     bn = to_sys(n, 2)
#     if bn.count('1') % 2 == 0:
#         bn = '10' + bn[2::] + '0'
#     else:
#         bn = '11' + bn[2::] + '1'
#     r = int(bn, 2)
#     if r > 50:
#         print(n)
#         break

#8
# from itertools import *
# count = 0
# products = product('01234567', repeat=5)
# for i in products:
#     p = ''.join(i)
#     if p[0] not in '01357' and p[-1] not in '26' and p.count('7') <= 2:
#         count += 1
# print(count)

#9
# file = open('../9_17628.txt')
# count = 0
# for line in file:
#     arr = [int(x) for x in line.split()]
#     m = max(arr)
#     p2 = [x for x in arr if arr.count(x) == 2]
#     if len(p2) == 2 and m < (sum(arr) - m):
#         count += 1
# print(count)

#12
# l = '9' * 100
# while '33333' in l or '999' in l:
#     if '33333' in l:
#         l = l.replace('33333', '99', 1)
#     else:
#         l = l.replace('999', '3', 1)
# print(l)

#13
# from ipaddress import *
# net = ip_network('172.16.128.0/255.255.192.0', False)
# count = 0
# for ip in net:
#     if f'{ip:b}'.count('1') % 2 != 0:
#         count += 1
# print(count)

#14
# m = -1
# for x in range(0, 2031):
#     n = 3**100 - x
#     n3 = to_sys(n, 3)
#     if n3.count('0') == 5:
#         m = x
# print(m)

#17
# file = open(r"C:\Users\Ivan\Downloads\17_17530.txt")
# arr = [int(x) for x in file]
# m = min(arr)
# count = 0
# ms = 100_001 * 2
# for i in range(0, len(arr) - 1):
#     n1 = arr[i]
#     n2 = arr[i + 1]
#     if n1 % 55 == m or n2 % 55 == m:
#         count += 1
#         ms = min(ms, n1 + n2)
# print(count, ms)

#19 - 21

# def f(s1, s2, m, c):
#     if c < m:
#         return 0
#
#     if s1 + s2 >= 65:
#         return m % 2 == c % 2
#
#     steps = [f(s1 + 1, s2, m + 1, c), f(s1, s2 + 1, m + 1, c), f(s1 * 3, s2, m + 1, c), f(s1, s2 * 3, m + 1, c)]
#
#     if (m + 1) % 2 == c % 2:
#         return any(steps)
#     else:
#         return all(steps)
#
# print('20:', [x for x in range(1, 59) if f(6, x, 0, 1) == 0 and f(6, x, 0, 3)])
# print('21:', [x for x in range(1, 59) if f(6, x, 0, 2) == 0 and f(6, x, 0, 4)])

#23
# def f(s, e):
#     if s < e:
#         return 0
#     if s == e:
#         return 1
#     return f(s - 1, e) + f(s // 2, e)
#
# print(f(30, 8) * f(8, 1))

#24
# file = open(r"C:\Users\Ivan\Downloads\24_17535.txt")
# s = file.read().strip()
# m = -1
# cds = []
# for i in range(0, len(s) - 1):
#     if s[i] == 'C' and s[i + 1] == 'D':
#         cds.append(i)
#     if len(cds) == 162 or i == len(s) - 1:
#         l = i - cds[0]
#         m = max(l, m)
#         cds = cds[1:]
#
# print(m)

#25
# count = 0
# i = 800_000
# while count != 5:
#     i += 1
#     mind = -1
#     maxd = -1
#     for j in range(2, i):
#         if i % j == 0:
#             mind = j
#             maxd = i // j
#             break
#     M = mind + maxd
#     if str(M)[-1] == '4':
#         print(i, M)
#         count += 1

#26
# file = open(r"C:\Users\Ivan\Downloads\26_17537.txt")
# n, m, k = map(int, (file.readline().split()))
# ryadi = [m + 1] * (k + 1)
# for i in range(0, n):
#     r1, m1 = map(int, file.readline().split())
#     ryadi[m1] = min(ryadi[m1], r1)
# for


# ДОДЕЛАТЬ + Шастин номер 2