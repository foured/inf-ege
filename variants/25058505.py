#2
# print('z y w x')
# for x in 0, 1:
#     for y in 0, 1:
#         for w in 0, 1:
#             for z in 0, 1:
#                 f = ((w <= y) <= x) or (not z)
#                 if f == 0:
#                     print(z, y, w, x)

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
# left(90)
# k=10
# for i in range(10):
#     forward(22*k)
#     right(90)
#     forward(6*k)
#     right(90)
# pu()
# forward(1*k)
# right(90)
# forward(5*k)
# left(90)
# pd()
# for i in range(10):
#     forward(53*k)
#     right(90)
#     forward(75*k)
#     right(90)
# pu()
# for x in range(-30, 30):
#     for y in range(-30, 30):
#         goto(x*k,y*k)
#         dot(5)
# exitonclick()

#8
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

#9
# file = open(r"C:\Users\Ivan\Downloads\9_17863.csv")
# count = 0
# for line in file:
#     arr = [int(x) for x in line.split(';')]
#     p3 = [x for x in arr if arr.count(x) == 3]
#     np = [x for x in arr if arr.count(x) == 1]
#     if len(p3) == 3 and len(np) == 3 and sum(p3)**2 > sum(np)**2:
#         count += 1
# print(count)

#12
# l = '1' * 81
#
# while '11111' in l or '888' in l:
#     if '11111' in l:
#         l = l.replace('11111', '88', 1)
#     else:
#         l = l.replace('888', '8', 1)
#
# print(l)

#13
# from ipaddress import *
# net = ip_network('172.16.168.0/255.255.248.0', False)
# count = 0
# for ip in net:
#     if f'{ip:b}'.count('1') % 5 != 0:
#         count += 1
# print(count)

#14
# m = -1
# for x in range(0, 19):
#     n1 = 9 * 19**7 + 8 * 19**6 + 8 * 19**5 + 9 * 19**4 + 7 * 19**3 + x * 19**2 + 2 * 19**1 + 1 * 19**0
#     n2 = 2 * 19**4 + x * 19**3 + 9 * 19**2 + 2 * 19**1 + 3 * 19**0
#     if (n1 + n2) % 18 == 0:
#         m = (n1 + n2) // 18
# print(m)

#16
# import sys
# sys.setrecursionlimit(10000)
# def f(n):
#     if n == 1:
#         return 1
#     return (n - 1) * f(n - 1)
# print((f(2024) + 2 * f(2023)) / f(2022))

#17
# file = open(r"C:\Users\Ivan\Downloads\17_17873.txt")
# arr = [int(x) for x in file]
# mini = min(arr)
# maxs = -1
# count = 0
# for i in range(0, len(arr) - 1):
#     n1 = arr[i]
#     n2 = arr[i + 1]
#     if n1 % 16 == mini or n2 % 16 == mini:
#         count += 1
#         maxs = max(maxs, n1 + n2)
# print(count, maxs)

#19-21
# def f(s, t, c):
#     if s <= 19:
#         return t % 2 == c % 2
#
#     if t >= c:
#         return 0
#
#     h = [f(s - 2, t + 1, c), f(s - 5, t + 1, c), f(s // 3, t + 1, c)]
#     return any(h) if (t + 1) % 2 == c % 2 else all(h)
#
# print('19: ', [s for s in range(20, 100) if f(s, 0, 1) == 0 and f(s, 0, 2)])
# print('20: ', [s for s in range(20, 100) if f(s, 0, 1) == 0 and f(s, 0, 3)])
# print('20: ', [s for s in range(20, 100) if f(s, 0, 2) == 0 and f(s, 0, 4)])

#23
# def f(n, c):
#     if n == c:
#         return 1
#     if n < c:
#         return 0
#     return f(n - 2, c) + f(n // 2, c)
#
# print(f(38, 16) * f(16, 2))

#24
# file = open(r"C:\Users\Ivan\Downloads\24_17878.txt")
# s = file.read().strip().replace('-*', '-;*').replace('*-', '*;-')\
#      .replace('**', '*;*').replace('--', '-;-').replace('-0-', '-;0-').replace('-0*', '-;0*')
# s = s.replace('-*', '-;*').replace('*-', '*;-')\
#      .replace('**', '*;*').replace('--', '-;-').replace('-0-', '-;0-').replace('-0*', '-;0*')
#
# ml = 0
# #for v in s.split(';'):
# print(max([len(x) for x in s.split(';')]))

#25
from fnmatch import *
for i in range(0, 10**10, 1917):
    if fnmatch(str(i), '3?12?14*5'):
        print(i, i // 1917)
