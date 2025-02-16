#2

# print('x y w z')
# for x in 0,1:
#     for y in 0,1:
#         for w in 0,1:
#             for z in 0,1:
#                 f = (y <= (not(x <= z))) or w
#                 if f == 0:
#                     print(x, y, w, z)

#5
# m = -1
# for n in range(1, 13):
#     bn = bin(n)[2::]
#     if n % 2 == 0:
#         bn = '10' + bn
#     else:
#         bn = '1' + bn + '01'
#     r = int(bn, 2)
#     m = max(m, r)
# print(m)

#6
# from turtle import *
# lt(90)
# size=10
# screensize(2000,2000)
# tracer(1, 0)
# down()
# for i in range(0, 3):
#     fd(7 * size)
#     right(90)
#     fd(12 * size)
#     right(90)
# up()
# fd(4 * size)
# right(90)
# fd(6 * size)
# left(90)
# down()
# for i in range(0, 4):
#     fd(83 * size)
#     right(90)
#     fd(77 * size)
#     right(90)
# up()
# for x in range(-100, 101):
#     for y in range(-100, 101):
#         goto(x * size, y * size)
#         dot(2)
#
# done()

#8
# from itertools import *
# ci = 0
# products = product('КОСУФ', repeat=5)
# for i in products:
#     p = ''.join(i)
#     ci += 1
#     if p.count('Ф') == 0 and p.count('У') == 2:
#         res = ci
# print(res)

#9
# file = open('../9_17628.txt')
# count = 0
# for line in file:
#     arr = [int(x) for x in line.split()]
#     p3 = [x for x in arr if arr.count(x) == 3]
#     np = [x for x in arr if arr.count(x) == 1]
#     if len(p3) == 3 and len(np) == 3 and (sum(p3) ** 2) > (sum(np) ** 2):
#         count += 1
# print(count)

#12
# l = '8' * 83
# while '111' in l or '88888' in l:
#     if '111' in l:
#         l = l.replace('111', '88', 1)
#     else:
#         l = l.replace('88888', '8', 1)
# print(l)

#13
# from ipaddress import *
# count = 0
# net = ip_network('112.160.0.0/255.240.0.0', False)
# for ip in net:
#     if f'{ip:b}'.count('1') % 3 != 0:
#         count += 1
# print(count)

def to_sys(num, sys):
    res = ''
    while num > 0:
        res = str(num % sys) + res
        num //= sys
    return res

#14
# m = -1
# for x in range(0, 2031):
#     n = 7**91 + 7**160 - x
#     n7 = to_sys(n, 7)
#     if n7.count('0') == 70:
#         m = max(m, x)
# print(m)

#15
# def f(x, a):
#     return (x % a == 0) or ((77 <= x <= 90) <= (x % 22 != 0))
# m = -1
# for a in range(1, 1000):
#     if all(f(x, a) for x in range(0, 1000)):
#         m = a
# print(m)

#16
# import sys
# sys.setrecursionlimit(10**8)
#
# def f(n):
#     if n == 1:
#         return 1
#     return 2 * n * f(n - 1)
#
# print((f(2024) // 16 - f(2023)) // f(2022))

#17
# file = open(r"C:\Users\Ivan\Downloads\17_17558.txt")
# arr = [int(x) for x in file]
# k32 = [x for x in arr if x % 32 == 0]
# lk32 = len(k32)
# count = 0
# ms = -100_001 * 2
# for i in range(0, len(arr) - 1):
#     n1 = arr[i]
#     n2 = arr[i + 1]
#     if (n1 < 0 or n2 < 0) and (n1 + n2) < lk32:
#         count += 1
#         ms = max(ms, n1 + n2)
# print(count)
# print(ms)

#19
# def f(s, t, c):
#     if s >= 58:
#         return t % 2 == c % 2
#
#     if t >= c:
#         return 0
#
#     h = [f(s + 1, t + 1, c), f(s + 4, t + 1, c), f(s * 2, t + 1, c)]
#     return any(h) if (t + 1) % 2 == c % 2 else all(h)
#
# print('19: ', [s for s in range(1, 57) if f(s, 0, 1) == 0 and f(s, 0, 2)])
# print('20: ', [s for s in range(1, 57) if f(s, 0, 1) == 0 and f(s, 0, 3)])
# print('20: ', [s for s in range(1, 57) if f(s, 0, 2) == 0 and f(s, 0, 4)])

#23
# def f(s, e):
#     if s == e:
#         return 1
#     if s > e:
#         return 0
#     return f(s + 1, e) + f(s + 2, e) + f(s + 3, e)
# print(f(5, 7) * f(7, 11))

#24
# file = open(r"C:\Users\Ivan\Downloads\24_17563.txt")
# l = file.read().strip().replace('8', '7').replace('9', '7').replace('-*', '-;*').replace('*-', '*;-')\
#     .replace('**', '*;*').replace('--', '-;-').replace('-07', '-0;7').replace('*07', '*0;7')\
#     .replace('-00', '-0;0').replace('*00', '*0;0').replace('-0', '-;0').replace('*0', '*;0')
# l = l.replace('8', '7').replace('9', '7').replace('-*', '-;*').replace('*-', '*;-')\
#     .replace('**', '*;*').replace('--', '-;-').replace('-07', '-0;7').replace('*07', '*0;7')\
#     .replace('-00', '-0;0').replace('*00', '*0;0').replace('-0', '-;0').replace('*0', '*;0')
# l = l.split(';')
# ml = 0
# lv = ''
# for v in l:
#     if len(v) > ml:
#         ml = len(v)
#         lv = v
# print(ml)
# print(lv)

# #25
# ns = []
# ms = []
# count = 0
# n = 700_000
# while count != 5:
#     mind = -1
#     maxd = -1
#     for i in range(2, int((n / 2) + 1)):
#         if n % i == 0:
#             mind = i
#             maxd = n // i
#             break
#     if maxd == -1:
#         m = 0
#     else:
#         m = mind + maxd
#     if str(m)[-1] == '4':
#         ns.append(n)
#         ms.append(m)
#         count += 1
#     n += 1
#
# print(ns)
# print(ms)

#26
# file = open(r"C:\Users\Ivan\Downloads\26_17565.txt")
# n, s = map(int, file.readline().split())
# chels = []
# class chel:
#     def __init__(self, id, oc1, oc2, oc3, sobes):
#         self.id = id
#         self.oc1 = oc1
#         self.oc2 = oc2
#         self.oc3 = oc3
#         self.sobes = sobes
#
#     def ocs(self):
#         return self.oc1 + self.oc2 + self.oc3
#
#     def __gt__(self, other):
#         return self.ocs() > other.ocs()
#
# for line in file.readlines():
#     d = [int(x) for x in line.split()]
#     chels.append(chel(d[0], d[1], d[2], d[3], d[4]))
#
# def get_chel(oc_sum):
#     cs = []
#     for c in chels:
#         if chels.ocs() == oc_sum:
#             cs.append(c)
#     return cs
#
#
# chels.sort(reverse=True)
# while s > 0:
#     for c in chels:
#