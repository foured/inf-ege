#2
from runpy import run_path


# print('a b c d')
# for a in 0, 1:
#     for b in 0, 1:
#         for c in 0, 1:
#             for d in 0, 1:
#                 f = ((a <= b) == c) or d
#                 if f == 0:
#                     print(a, b, c, d)


def to_sys(n, osn):
    alf = '0123456789ABCDEF'
    res = ''
    while n > 0:
        res = alf[n % osn] + res
        n //= osn
    return res

#5

# mr = 10**8
# for n in range(1, 10_000):
#     tn = to_sys(n, 3)
#     sc =  sum([int(x) for x in tn])
#     if sc % 2 == 0:
#         tn = '1' + tn + '2'
#     else:
#         tn = '2' + tn + '0'
#     r = int(tn, 3)
#     if r > 100:
#         mr = min(r, mr)
# print(mr)

#6

# from turtle import *
#
# k = 10
# left(90)
# tracer(0)
# pu()
# goto(-35 * k, -35 * k)
# pd()
# for i in range(9):
#     fd(50 * k)
#     right(90)
#     fd(35 * k)
#     right(90)
# pu()
# fd(5 * k)
# right(90)
# fd(10 * k)
# right(90)
# pd()
# for i in range(4):
#     fd(35 * k)
#     right(90)
#     fd(17 * k)
#     right(90)
# pu()
# for x in range(-50, 50):
#     for y in range(-50, 50):
#         goto(x * k, y * k)
#         dot(2)
# done()

#8

# from itertools import product
# ps = product('ЕЛОПРСТ', repeat=5)
# count = 0
# n = 0
# for i in ps:
#     p = ''.join(i)
#     n += 1
#     if n % 2 == 1 and p[-1] in 'ЕО' and len([c for c in p if c in 'ЛПРСТ']) <= 3:
#         count += 1
# print(count)

#9

# file = open(r"C:\Users\Ivan\Downloads\9_18174.txt")
# count = 0
# for line in file:
#     arr = [int(x) for x in line.split()]
#     p2 = [x for x in arr if arr.count(x) == 2]
#     o = [abs(x) for x in arr if x < 0]
#     p = [x for x in arr if x > 0]
#     if len(p2) == 2 and len(set(arr)) == 5 and sum(o) > sum(p):
#         count += 1
# print(count)

#12

# ms = -1
# for n in range(4, 10_000):
#     l = '4' + '1' * n
#     while '411' in l or '1111' in l:
#         if '411' in l:
#             l = l.replace('411', '14', 1)
#         if '1111' in l:
#             l = l.replace('1111', '1', 1)
#     s = sum([int(x) for x in l])
#     ms = max(ms, s)
# print(ms)

#13

# from ipaddress import *
#
# ip = ip_address('205.154.212.20')
# nip = ip_address('205.154.192.0')
#
# for mask in range(33):
#     net = ip_network(f'{ip}/{mask}', False)
#     if net.network_address == nip:
#         print(mask)
#'11111111 11111111 11000000 00000000'
#'11111111 11111111 11100000 00000000'

#14

# for x in range(0, 5555):
#     n = 5**150 + 5**135 - x
#     n5 = to_sys(n, 5)
#     if n5.count('4') == 134:
#         print(x)

#15

# def f(x, a):
#     return ( x % 7 != 0 and x % 13 == 0) <= (x > a - 40)
#
# for a in range(1, 1000):
#     if all(f(x, a) for x in range(1, 1000)):
#         print(a)

#16

# def f(n):
#     if n >= 2010:
#         return n
#     return f(n + 3) + f(n + 2) + f(n + 1)
#
# print( (f(2000) - 2 * (f(2002) + f(2003))) / f(2004) )

#17

# file = open(r"C:\Users\Ivan\Downloads\17_18176.txt")
# arr = [int(x) for x in file.readlines()]
# mv = min([x for x in arr if x > 0 and str(x)[-1] == '4'])
# ms = -100_001 * 3
# count = 0
# for i in range(0, len(arr) - 2):
#     n1, n2, n3 = arr[i], arr[i + 1], arr[i + 2]
#     s = sum([int(x) for x in str(abs(n1))]) + sum([int(x) for x in str(abs(n2))]) + sum([int(x) for x in str(abs(n3))])
#     if s == mv:
#         count += 1
#         ms = max(ms, n1 + n2 + n3)
# print(count)
# print(ms)

#19 - 21

# def f(s1, s2, h, c):
#     if s1 + s2 >= 77:
#         return h % 2 == c % 2
#
#     if h >= c:
#         return 0
#
#     steps = [f(s1 + 3, s2, h + 1, c), f(s1 * 3, s2, h + 1, c), f(s1, s2 + 3, h + 1, c), f(s1, s2 * 3, h + 1, c)]
#
#     if h % 2 != c % 2:
#         return any(steps)
#     else:
#         return all(steps)
#
# print('19:', [x for x in range(1, 65) if f(12, x, 0, 1) == 0 and f(12, x, 0, 2)])
# print('20:', [x for x in range(1, 65) if f(12, x, 0, 1) == 0 and f(12, x, 0, 3)])
# print('21:', [x for x in range(1, 65) if f(12, x, 0, 2) == 0 and f(12, x, 0, 4)])

#23

# from math import *
#
# def f(s, e):
#     if s == e:
#         return 1
#     if s < e:
#         return 0
#     return f(s - 4, e) + f(s - 7, e) + f(int(sqrt(s)), e)
#
# print(f(44, 22) * f(22, 3))

#24

# file = open(r"C:\Users\Ivan\Downloads\24_18186 (1).txt")
# s = file.read().strip().replace('E', 'A').replace('C', 'B').replace('D', 'B').replace('F', 'B')\
#     .replace('F', 'B').replace('G', 'B').replace('H', 'B')
# lp = -1
# ml = -1
# for i in range(len(s) - 2):
#     c1, c2, c3 = s[i], s[i + 1], s[i + 2]
#     if c1 == 'B' and c2 == 'B' and c3 == 'A':
#         if lp != -1:
#             ml = max(ml, i - lp + 2 + 1)
#         lp = i
# print(ml)

#25

from math import *

def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

n = 1_000_000
count = 0
while count < 5:
    n += 1
    pc = 0
    mpd = -1
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            d1, d2 = i, n // i
            if is_prime(d1):
                pc += 1
                mpd = max(mpd, d1)
            if is_prime(d2):
                pc += 1
                mpd = max(mpd, d2)
    if pc == 3:
        print(n, mpd)
        count += 1
