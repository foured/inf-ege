#2
from itertools import repeat


# print('x y w z')
# for x in 0, 1:
#     for y in 0, 1:
#         for w in 0, 1:
#             for z in 0, 1:
#                 f = y and (x or z) or (not(y or z)) or w
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
# m = -1
# for n in range(1, 100, 2):
#     bn = bin(n)[2:]
#     ost = n % 5
#     if ost == 0:
#         bn = bn[:3] + bn
#     else:
#         ost *= 5
#         bn += bin(ost)[2:]
#     r = int(bn, 2)
#     if r < 313:
#         m = n
# print(m)

#6
# from turtle import *
# left(90)
# k=10
# tracer(1, 0)
# for i in range(2):
#     fd(11 * k)
#     right(90)
#     fd(17 * k)
#     right(90)
# pu()
# fd(7 * k)
# left(90)
# bk(1 * k)
# right(90)
# pd()
# for i in range(2):
#     fd(15 * k)
#     right(90)
#     fd(7 * k)
#     right(90)
# pu()
# for x in range(-30, 30):
#     for y in range(-30, 30):
#         goto(x*k,y*k)
#         dot(5)
# exitonclick()

#8
# from itertools import product, repeat
#
# count = 0
# products = product('ЛЮСТРА', repeat=5)
# for i in products:
#     p = ''.join(i)
#     if p.count('Ю') <= 2 and p[-1] in 'ЮА':
#         count += 1
# print(count)

#9
# file = open(r"C:\Users\Ivan\Downloads\9_17968.txt")
# count = 0
# for line in file:
#     arr = [int(x) for x in line.split()]
#     c = [x for x in arr if x % 2 == 0]
#     nc = [x for x in arr if x % 2 != 0]
#     if max(arr) < (sum(arr) - max(arr)) and sum(c) == sum(nc):
#         count += 1
# print(count)

#12
# l = '3' * 111
# while '33333' in l or '1111' in l:
#     if '33333' in l:
#         l = l.replace('33333', '111', 1)
#     else:
#         l = l.replace('111', '33', 1)
# print(l)
# print(sum([int(x) for x in l]))

#16
# import sys
# sys.setrecursionlimit(10**8)
# def f(n):
#     if n < 5:
#         return 4*4
#     return 4 * f(n - 4) + 4
# print(f(4048) / f(4036))

#17
# file = open(r"C:\Users\Ivan\Downloads\17_18045.txt")
# arr = [int(x) for x in file.readlines()]
# nodc = len([x for x in arr if len(str(x)) == 2])
# count = 0
# ms = 100_001 * 2
# for i in range(0, len(arr) - 1):
#     n1 = arr[i]
#     n2 = arr[i + 1]
#     if (int(str(n1)[-1]) + int(str(n2)[-1])) == nodc:
#         count += 1
#         ms = min(ms, n1 + n2)
# print(count)
# print(ms)

#19-21
# def f(s, t, c):
#     if s <= 17:
#         return t % 2 == c % 2
#
#     if t >= c:
#         return 0
#
#     h = [f(s - 3, t + 1, c), f(s - 5, t + 1, c), f(s // 2, t + 1, c)]
#     #return any(h) if (t + 1) % 2 == c % 2 else all(h)
#     if t % 2 != c % 2:
#         return any(h)
#     return all(h)
#
# print('19: ', [s for s in range(18, 50) if f(s, 0, 1) == 0 and f(s, 0, 2)])
# print('20: ', [s for s in range(18, 100) if f(s, 0, 1) == 0 and f(s, 0, 3)])
# print('21: ', [s for s in range(18, 100) if f(s, 0, 2) == 0 and f(s, 0, 4)])

#23
# def f(s, e):
#     if s == 24 or s < e:
#         return 0
#     if s == e:
#         return 1
#     return f(s - 2, e) + f(s - 3, e) + f(s // 4, e)
# print(f(36, 13))

#24
#file = open(r"C:\Users\Ivan\Downloads\24_18029.txt")
# s = file.read().strip().replace('X', ' ')
# ss = [y for y in s.split()]
# my = -1
# for cs in ss:
#     my = max(my, cs.count('Y'))
# for cs in ss:
#     if cs.count('Y') == my:
#         print(cs)
#         print(len(cs) + 2)
#

#25
# for x in range(1000, 10000):
#     sd = 0
#     for i in range(1, x + 1):
#         if x % i == 0:
#             sd += i
#     if str(sd)[-2:] == '23':
#         print(x, sd)

#26
file = open(r"C:\Users\Ivan\Downloads\26_18030.txt")
n = int(file.readline())
arr = [int(x) for x in file.readlines()]
cf = 0
uc = 0
