# def f(x, a):
#     return ((x&28 != 0) or (x&45 != 0)) <= ((x&17 == 0) <= (x & a != 0))
#
# for a in range(0, 100):
#     if all(f(x, a) for x in range(0, 100)):
#         print(a)
#         break

# def f(x, y, a):
#     return (x + 3*y > a) or (y < 30) or (x < 30)
#
# m = -1
# for a in range(0, 1000):
#     if all(f(x, y, a) for x in range(0, 1000) for y in range(0, 1000)):
#         m = max(m, a)
# print(m)

# def f(x, a):
#     return (x % a == 0) or ((x in range(70, 91)) <= (x % 27 != 0))
#
# m = -1
# for a in range(1, 1000):
#     if all(f(x, a) for x in range(1, 1000)):
#         m = max(m, a)
# print(m)

# def f(x, a):
#     return (x&9 == 0) <= ((x&19 != 0) <= (x&a !=0))
#
# for a in range(0, 1000):
#     if all(f(x, a) for x in range(0, 1000)):
#         print(a)
#         break

# def f(x, y, a):
#     return ((x + y) <= 22) or (y <= (x - 6)) or(y >= a)
# m = 0
# for a in range(0, 1000):
#     if all(f(x, y, a) for x in range(0, 1000) for y in range(0, 1000)):
#         m = max(m, a)
#
# print(m)

# def t(s1, s2, s3):
#     arr = [s1, s2, s3]
#     arr.sort()
#     return arr[0] + arr[1] > arr[2]
#
# def f(x, a):
#     return not((t(x, 11, 18) == (not(max(x, 5) > 68))) and t(x, a, 5))
#
# for a in range(1, 1000):
#     if all(f(x, a) for x in range(1, 1000)):
#         print(a)
#

def f(A, x):
    return (x % 10 == 4) <= (x > (A - 11))
m = -1
for A in range(1, 100):
    if all(f(A, x) for x in range(1, 100)):
        m = max(m, A)
print(m)