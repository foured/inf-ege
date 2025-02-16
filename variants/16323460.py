#---2
# print('x y w z')
# for x in 0, 1:
#     for y in 0, 1:
#         for w in 0, 1:
#             for z in 0, 1:
#                 f = ((x and y) or (y and z)) == ((x <= w) and (w <= z))
#                 if f and x == 0 and w == 1:
#                     print(x, y, w, z)

#---5
# for n in range(2, 10000):
#     bn = bin(n)[2::]
#     bn = bn[:-1]
#     if n % 2 == 0:
#         bn += '01'
#     else:
#         bn += '10'
#     r = int(bn, 2)
#     if r == 2018:
#         print(n)
#         break

#---6
# from turtle import *
# left(90)
# speed(1000)
# k=30
# for i in range(4):
#     forward(12*k)
#     right(90)
# for i in range(3):
#     forward(12*k)
#     right(120)
# pu()
# for x in range(13):
#     for y in range(13):
#         goto(x*k,y*k)
#         dot(5)
# exitonclick()

# count = 0
# for x in range(1, 12):
#     for y in range(1, 12):
#         if y < (x / 3**0.5) or y > ((-x / 3**0.5) + 12):
#             count += 1
# print(count)

#---8
# from itertools import product
#
# count = 0
# products = product('01234567', repeat=5)
# for i in products:
#     p = ''.join(i)
#
#     npv = [x for x in p if p.count(x) == 1]
#
#     if p[0] != '0' and len(npv) == 5:
#         flag = True
#         for i in range(0, len(npv) - 1):
#             cp = int(p[i])
#             np = int(p[i + 1])
#             if cp % 2 == np % 2:
#                 flag = False
#                 break
#         if flag:
#             count += 1
# print(count)

#---9
# with open(r'C:\Users\Ivan\Downloads\9.csv', encoding='utf-8-sig') as file:
#     count = 0
#     for line in file:
#         arr = [int(x) for x in line.strip().split(';')]
#         p2 = [x for x in arr if arr.count(x) == 2]
#         np = [x for x in arr if arr.count(x) == 1]
#
#         if len(np) == 3 and len(p2) == 4 and (sum(np) / 3 < sum(p2) / 4):
#             count += 1
#     print(count)

#---12
# from itertools import product
#
# def proc(w :str):
#     while '11' in w:
#         if '112' in w:
#             w = w.replace('112', '6', 1)
#         else:
#             w = w.replace('11', '3', 1)
#     return w
#
# m = 0
# products = product('12', repeat=14)
# for i in products:
#     p = ''.join(i)
#     if p.count('1') == 10 and p.count('2') == 4:
#         p = proc(p)
#         ip = [int(x) for x in p]
#         s = sum(list(ip))
#         m = max(m, s)
# print(m)

#---13
# from ipaddress import *
#
# net = ip_network('146.212.200.55/255.255.240.0', False)
# print(net.network_address)

#---14
# count = 0
# r = 49**7 + 7**20 - 28
# while r > 0:
#     if r % 7 == 6:
#         count += 1
#     r //= 7
# print(count)

#---15
# def f(x, y, a):
#     return (a <= (x**2 <= 81)) and ((y**2 <= 36) <= a)
#
# for a in range(0, 1000):
#     if all(f(x, y, a) for x in range(0, 1000) for y in range(0, 1000)):
#         print(a)
#         break

#---16
# def f(n):
#     if n == 0:
#         return 0
#     if n % 2 != 0:
#         return f(n-1) + 1
#     else:
#         return f(n//2)
#
# count = 0
# for n in range(1, 1_000_000_000):
#     if f(n) == 2:
#         count += 1
# print(count)

#---17
# with open(r"C:\Users\Ivan\Downloads\17.txt") as file:
#     arr = [int(x) for x in file]
#     count = 0
#     ms = -10001 * 2
#     for i in range(0, len(arr) - 1):
#         n1 = arr[i]
#         n2 = arr[i + 1]
#         if (n1 + n2) % 7 == 0 and (n1 % 5 == 0 or n2 % 5 == 0):
#             count += 1
#             ms = max(ms, n1 + n2)
#     print(count)
#     print(ms)