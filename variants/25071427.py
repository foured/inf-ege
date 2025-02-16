#2
# print('x y w z')
# for x in 0, 1:
#     for y in 0, 1:
#         for w in 0, 1:
#             for z in 0, 1:
#                 f = ((x <= z) <= w) or (not y)
#                 if f == 0:
#                     print(x, y, w, z)
# #5
# for n in range(1_000, 10_000):
#     n1, n2, n3, n4 = [int(x) for x in str(n)]
#     r1, r2, r3 = n1 * n2, n1 * n3, n1 * n4
#     m1, m2 = max(r1, r2), max(r2, r3)
#     mr1, mr2 = min(m1, m2), max(m1, m2)
#     r = int(str(mr1) + str(mr2))
#     if r == 5472:
#         print(n)
#         break

#6
# from turtle import *
#
# k = 20
# tracer(0)
# pu()
# goto(-5 * k, 10 * k)
# pd()
# for i in range(2):
#     fd(10 * k)
#     right(90)
#     fd(20 * k)
#     right(90)
# pu()
# bk(4 * k)
# right(90)
# fd(7 * k)
# left(90)
# pd()
# for i in range(4):
#     fd(8 * k)
#     left(90)
#     fd(12 * k)
#     left(90)
# pu()
# fd(10 * k)
# pd()
# for i in range(4):
#     fd(12 * k)
#     right(90)
# pu()
# for x in range(-50, 50):
#     for y in range(-50, 50):
#         goto(x * k, y * k)
#         dot(3)
# done()

#8
# from itertools import product
#
# c = 0
# ps = product(set('дионисий'), repeat=6)
# for i in ps:
#     p = ''.join(i)
#     if ('д' in p) + ('н' in p) == 1:
#         can = True
#         for j in range(len(p) - 1):
#             c1, c2 = p[j], p[j + 1]
#             if c1 == c2:
#                 can = False
#                 break
#         if can:
#             c += 1
# print(c)

#9
# f = open('files/9_18943.txt')
# c = 0
# for line in f:
#     arr = [int(x) for x in line.split()]
#     p3 = [x for x in arr if arr.count(x) == 3]
#     p2 = [x for x in arr if arr.count(x) == 2]
#     p1 = [x for x in arr if arr.count(x) == 1]
#     if len(p3) == 3 and len(p2) == 2 and len(p1) == 2 and (sum(set(p3)) + sum(set(p2)) >= sum(p1)):
#         c += 1
# print(c)

#17
# f = open(r"C:\Users\Ivan\Downloads\17_18957.txt")
# arr = [int(x) for x in f.readlines()]
# ma = max(arr)
# c = 0
# ms = -(10**8)
# for i in range(len(arr) - 2):
#     n1, n2, n3 = arr[i], arr[i + 1], arr[i + 2]
#     zs = 0
#     if '0' in str(n1): zs += 1
#     if '0' in str(n2): zs += 1
#     if '0' in str(n3): zs += 1
#     if zs <= 1 and (n1 + n2 + n3) < (ma / 2):
#         c += 1
#         ms = max(n1 + n2 + n3, ms)
# print(c)
# print(ms)


#19-21
# def game(s, h, c):
#     if h > c:
#         return 0
#     if s > 665:
#         return h % 2 == c % 2
#     v = [game(s + 3, h + 1, c), game(s * 3, h + 1, c), game(s + s**2, h + 1, c)]
#
#     if h % 2 != c % 2:
#         return any(v)
#     return all(v)
#
# print('19:', [s for s in range(1, 666) if game(s, 0, 1) == 0 and game(s, 0, 2) == 1]) # 5
# print('20:', [s for s in range(1, 666) if game(s, 0, 1) == 0 and game(s, 0, 3) == 1]) # 8 22
# print('21:', [s for s in range(1, 666) if game(s, 0, 2) == 0 and game(s, 0, 4) == 1]) # 19

#23
# def f(s, e):
#     if s == e:
#         return 1
#     if s < e or s == 40:
#         return 0
#     return f(s - 3, e) + f(s // 2, e) + f(s // 5, e)
#
# print(f(120, 49) * f(49, 6))

#BCADEFBACDFAB
#24
f = open(r"C:\Users\Ivan\Downloads\24_18530.txt")
s = f.read()
s = 'A' + 'BBDABCADEFBACDFAB' + 'A'
As = [i for i in range(len(s)) if s[i] == 'A' or s[i] == 'E']
last_d = 0
sub = 0
start_pos = 0
max_len = -1
for i in range(1, len(As) - 2):
    a1, a2 = As[i], As[i + 1]
    d = a2 - a1
    if d - last_d != sub:
        max_len = max(max_len, As[i + 2] - start_pos + 1)
        start_pos = As[i] + 1
        sub = d - last_d
    last_d = d
print(max_len)
