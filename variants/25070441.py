#2
# print('s r a t')
# for s in 0, 1:
#     for r in 0, 1:
#         for a in 0, 1:
#             for t in 0, 1:
#                 f = (s or (not r)) and (not(r == a)) and t
#                 if f:
#                     print(s, r, a, t)

#5
# m = -1
# for n in range(1, 26):
#     bn = bin(n)[2:]
#     if n % 2 != 0:
#         bn = '10' + bn + '1'
#     else:
#         bn = '10' + bn + '0111'
#     r = int(bn, 2)
#     m = max(m, r)
#     print(n)
# print(m)

#6
# from turtle import *
# tracer(0)
# k = 20
# pu()
# goto(-15 * k, 15 * k)
# pd()
# for i in range(13):
#     fd(13 * k)
#     right(90)
#     fd(5 * k)
# pu()
# right(90)
# fd(7 * k)
# left(90)
# fd(10 * k)
# pd()
# for i in range(23):
#     fd(8 * k)
#     left(90)
#     fd(11 * k)
#     left(90)
# pu()
# for x in range(-50, 50):
#     for y in range(-50, 50):
#         goto(x * k, y * k)
#         dot(3)
# done()

#8
# from itertools import product, repeat
#
# c = 0
# ps = product('ВЬЮГА', repeat=6)
# for i in ps:
#     p = ''.join(i)
#     if 'ЮГ' in p:
#         c += 1
# print(c)

#9
f = open(r"D:\Python\informatics\9_17628.txt")
c = 0
for line in f:
    arr = [int(x) for x in line.strip().split()]
    p3 = [x for x in arr if arr.count(x) == 3]
    np = [x for x in arr if arr.count(x) == 1]
    pp = [x * x for x in p3]
    y1 = (len(p3) == 3 and len(np) == 3)
    y2 = (sum(pp) > sum(np)**2)
    if (y1 + y2) == 0:
        c += 1
    else:
        print(arr, y1, y2)
print(c)

#13
# from ipaddress import *
# net = ip_network('192.168.248.176/255.255.255.240', False)
# c = 0
# for ip in net:
#     if f'{ip:b}'.count('1') == f'{ip:b}'.count('0'):
#         c += 1
# print(c)

#16
# f = [0] * 5000
# for n in range(len(f)):
#     if n <= 3:
#         f[n] = n - 1
#     elif n % 2 == 0:
#         f[n] = f[n - 2] + n // 2 - f[n - 4]
#     else:
#         f[n] = f[n - 1] * n + f[n - 2]
#
# print(f[4952] + 2 * f[4958] + f[4964])