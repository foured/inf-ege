# print('x y w z')
# for x in 0, 1:
#     for y in 0, 1:
#         for w in 0, 1:
#             for z in 0, 1:
#                 if not( ((w <= y) <= x) or (not z) ):
#                     print(x, y, w, z)
from itertools import product, permutations


# print('x y w z')
# for x in 0, 1:
#     for y in 0, 1:
#         for w in 0, 1:
#             for z in 0, 1:
#                 f = (x == (y <= (z or x))) and w
#                 if f:
#                     print(x, y, w, z)

# from itertools import *
# def f(x, y, w, z):
#     return ((x <= z) <= w) or (not y)
#
# for a in product([0, 1], repeat=7):
#     table = [(a[0], a[1], 1,    a[2]),
#              (a[3], 0,    a[4], a[5]),
#              (a[6], 1,    0,     0)]
#     if len(table) == len(set(table)):
#         for p in permutations('xywz'):
#             if [f(**dict(zip(p, st))) for st in table] == [0, 0, 0]:
#                 print(p)

# 18576
# def f(x, y, w, z):
#     return (not (w <= (x == (y or y)))) and (z <= x)
#
# for a in product([0, 1], repeat=5):
#     table = [(a[0], 1, 1, a[1]),
#              (0, a[2], a[3], 0),
#              (a[4], 0, 1, 0)]
#     if len(table) == len(set(table)):
#         for i in permutations('xywz'):
#             if [f(**dict(zip(i, st))) for st in table] == [1, 1, 1]:
#                 print(i)

# 18482
# def f(x, y, w, z):
#     return (x == (y <= (z or x))) and w
#
# for a1, a2, a3, a4, a5 in product([0, 1], repeat=5):
#     table = [(1, 0, 1, a1),
#              (0, a2, a3, 0),
#              (1, 0, a4, a5)]
#
#     if len(table) == len(set(table)):
#         for i in permutations('xywz'):
#             if [f(**dict(zip(i, st))) for st in table] == [1, 1, 1]:
#                 print(i)

# def f(x, y, w, z):
#     return ((not x) and y and z and (not w)) or ((not x) and y and (not z) and (not w)) or (x and y and z and (not w))
#
# for a in product([0, 1], repeat=7):
#     table = [(1, a[0], a[1], a[2]),
#              (0, a[3], 1, a[4]),
#              (a[5], 0, 0, a[6])]
#     if len(table) == len(set(table)):
#         for i in permutations('xywz'):
#             if [f(**dict(zip(i, st))) for st in table] == [1, 1, 1]:
#                 print(i)

def f(x, y, w, z):
    return (not (((not x) or y) and (not w))) or (not (z and (not(y and w))))

for a in product([0, 1], repeat=7):
    table = [
        (0, a[0], a[1], 1),
        (a[2], 1, a[3], a[4]),
        (1, 0, a[5], a[6])
    ]

    if len(table) == len(set(table)):
        for i in permutations('xywz'):
            if [f(**dict(zip(i, st))) for st in table] == [0, 0, 0]:
                print(i)