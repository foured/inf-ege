# file = open(r"C:\Users\Ivan\Downloads\26_17786.txt")
# n, v = map(int, file.readline().split())
# v *= 1000
# count = 0
# arr = sorted([int(x) for x in file if (7000 <= int(x) <= 12000)], reverse=True)
# for a in arr:
#     if a < v:
#         v -= a
#         count += 1
#         la = a
# print(count)
# print(la)
from itertools import count
from traceback import print_tb

#17537
# file = open(r"C:\Users\Ivan\Downloads\26_17537 (1).txt")
# N, M, K = map(int, file.readline().split())
# min_r = [M + 1] * (K + 1)
# for line in file.readlines():
#     r, m = map(int, line.split())
#     min_r[m] = min(min_r[m], r)
# mr, mm = -1, -1
# for i in range(1, K):
#     mr = max(mr, min(min_r[i] - 1, min_r[i + 1] - 1))
# for i in range(1, K):
#     r = max(mm, min(min_r[i] - 1, min_r[i + 1] - 1))
#     if r == mr:
#         mm = i
# print(mr, mm)

#17643
# file = open(r"C:\Users\Ivan\Downloads\26_17643.txt")
# N = int(file.readline())
# p = [-1] * 100_001
# zs = [0] * 100_001
# os = [0] * 100_001
#
# for line in file.readlines():
#     id, cp, s = map(int, line.split())
#     p[id] = cp
#     if s == 1:
#         os[id] += 1
#     else:
#         zs[id] += 1
#
# print(max(zs))
# for i in range(0, 100_001):
#     if zs[i] == max(zs):
#         print(i, p[i], os[i])

# 51
# 37134 831 0
# 46481 856 36
# 51786 856 37

# file = open(r"C:\Users\Ivan\Downloads\26.txt")
# #file = open('files/26.txt')
# N, M = map(int, file.readline().split())
# s = []
# a = []
# mc = 0
# m = -1
# for i in range(N):
#     s.append(int(file.readline()))
# for i in range(M):
#     mv = int(file.readline())
#     v = max([x for x in s if x <= mv])
#     a.append(v)
#     if mc < a.count(v):
#         mc = a.count(v)
#         m = v
# print(int(sum(a) / M))
# print(m)

# file = open(r"C:\Users\Ivan\Downloads\26_18492.txt")
# file.readline()
# arr = [int(x) for x in file.read().split()]
# m = -1
# for i in range(2, len(arr), 3):
#     m = max(m, arr[i])
# time = [0] * m
# for i in range(0, len(arr) - 3, 3):
#     n, t1, t2 = arr[i], arr[i + 1], arr[i + 2]
#     for j in range(t1, t2):
#         time[j] += 1
# mt = max(time)
# n = 0
# for i in range(0, len(time) - 1):
#     if time[i] == mt and time[i + 1] != mt:
#         n += 1
# print(n)

file = open(r"C:\Users\Ivan\Downloads\26-11.txt")
s, n = map(int, file.readline().split())
arr = sorted([int(x) for x in file.readlines()])
c = 0
lv = 0
m = 0
for v in arr:
    if s >= v:
        s -= v
        c += 1
        lv = v
        m = max(m, v)
    elif s + lv >= v:
        s += lv - v
        lv = v
        m = max(m, v)
print(c, m)