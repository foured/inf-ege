# def f(s, t, c):
#     if s <= 19:
#         return t % 2 == c % 2
#     if t >= c:
#         return 0
#     h = [f(s - 2, t + 1, c), f(s - 5, t + 1, c), f(s // 3, t + 1, c)]
#
#     if (t + 1) % 2 == c % 2:
#         return any(h)
#     else:
#         return all(h)
#
# print('19: ', [s for s in range(20, 100) if f(s, 0, 1) == 0 and f(s, 0, 2)])
# print('20: ', [s for s in range(20, 100) if f(s, 0, 1) == 0 and f(s, 0, 3)])
# print('21: ', [s for s in range(20, 100) if f(s, 0, 2) == 0 and f(s, 0, 4)])

# def f(s, t, c):
#     if s >= 54:
#         return t % 2 == c % 2
#     if t >= c:
#         return 0
#
#     h = [f(s + 2, t + 1, c), f(s * 2, t + 1, c)]
#
#     return any(h) if (t + 1) % 2 == c % 2 else all(h)
#
# print('19: ', [s for s in range(1, 54) if f(s, 0, 1) == 0 and f(s, 0, 2)])
# print('20: ', [s for s in range(1, 54) if f(s, 0, 1) == 0 and f(s, 0, 3)])
# print('20: ', [s for s in range(1, 54) if f(s, 0, 2) == 0 and f(s, 0, 4)])

# def f(a, b, t, c):
#     if (a + b) >= 65:
#         return t % 2 == c % 2
#     if t >= c:
#         return 0
#
#     h = [f(a + 1, b, t + 1, c), f(a, b + 1, t + 1, c), f(a * 3, b, t + 1, c), f(a, b * 3, t + 1, c)]
#
#     return any(h) if (t + 1) % 2 == c % 2 else all(h)
#     # return any(h)
#
# print('20: ', [s for s in range(1, 59) if f(6, s, 0, 1) == 0 and f(6, s, 0, 3)])
# print('21: ', [s for s in range(1, 59) if f(6, s, 0, 2) == 0 and f(6, s, 0, 4)])

# def f(a, b, t, c):
#     if (a + b) >= 123:
#         return t % 2 == c % 2
#
#     if t >= c:
#         return 0
#
#     h = [f(a + 1, b, t + 1, c), f(a, b + 1, t + 1, c), f(a * 2, b, t + 1, c), f(a, b * 2, t + 1, c)]
#
#     # return any(h)
#     return any(h) if (t + 1) % 2 == c % 2 else all(h)
#
# #print('19: ', [s for s in range(1, 110) if f(13, s, 0, 1) == 0 and f(13, s, 0, 2)])
# print('20: ', [s for s in range(1, 110) if f(13, s, 0, 1) == 0 and f(13, s, 0, 3)])
# print('21: ', [s for s in range(1, 110) if f(13, s, 0, 2) == 0 and f(13, s, 0, 4)])

# def f(s, t, c):
#     if s >= 435:
#         return t % 2 == c % 2
#
#     if t >= c:
#         return 0
#
#     h = [f(s + 5, t + 1, c), f(s * 3, t + 1, c)]
#     return any(h) if (t + 1) % 2 == c % 2 else all(h)
#
# print('19: ', [s for s in range(1, 435) if f(s, 0, 1) == 0 and f(s, 0, 2)])
# print('20: ', [s for s in range(1, 435) if f(s, 0, 1) == 0 and f(s, 0, 3)])
# print('20: ', [s for s in range(1, 435) if f(s, 0, 2) == 0 and f(s, 0, 4)])
#
# # ДЗ - вариант с https://kompege.ru/archive + доделать номер 24
#
# def f(s, t, c):
#     if s >= 435:
#         return t % 2 == c % 2
#
#     if t >= c:
#         return 0
#
#     h = [f(s + 1, t + 1, c), f(s + 2, t + 1, c), f(s * 2, t + 1, c)]
#     return any(h) if (t + 1) % 2 == c % 2 else all(h)
#
# print('19: ', [s for s in range(1, 435) if f(s, 0, 1) == 0 and f(s, 0, 2)])
# print('20: ', [s for s in range(1, 435) if f(s, 0, 1) == 0 and f(s, 0, 3)])
# print('20: ', [s for s in range(1, 435) if f(s, 0, 2) == 0 and f(s, 0, 4)])

# def f(s, h, c):
#     if s >= 313:
#         return h % 2 == c % 2
#
#     if h > c:
#         return 0
#
#     steps = [f(s + 2, h + 1, c), f(s + 3, h + 1, c), f(s * 3, h + 1, c)]
#
#     if h % 2 != c % 2:
#         return any(steps)
#     else:
#         return all(steps)
#
# print('19:', sum([s for s in range(1, 313) if f(s, 0, 1) == 0 and f(s, 0, 2)]))
# print('20:', [s for s in range(1, 313) if f(s, 0, 1) == 0 and f(s, 0, 3)])
# print('21:', sum([s for s in range(1, 313) if f(s, 0, 2) == 0 and f(s, 0, 4)]))

def f(s, t, c):
    if t > c:
        return 0
    if s >= 132:
        return t % 2 == c % 2
    h = [f(s + 3, t + 1, c), f(s + 6, t + 1, c), f(s * 3, t + 1, c)]
    if t % 2 == c % 2:
        return all(h)
    return any(h)

print('19:', [s for s in range(1, 132) if f(s, 0, 1) == 0 and f(s, 0, 2) == 1])
print('20:', [s for s in range(1, 132) if f(s, 0, 1) == 0 and f(s, 0, 3) == 1])
print('21:', [s for s in range(1, 132) if f(s, 0, 2) == 0 and f(s, 0, 4) == 1])