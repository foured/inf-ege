# def f(n, t):
#     if n == t:
#         return 1
#     if n > t or n == 15:
#         return 0
#     return f(n + 1, t) + f(n + 2, t)
#
# print(f(3, 9) * f(9, 20))

def f(s, e):
    if s == e:
        return 1
    if s > e:
        return 0

    return f(s + 3, e) + f(s + max([int(x) for x in str(s)]), e)
print(f(10, 24) * f(24, 41))