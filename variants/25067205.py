#2
# print('x y w z')
# for x in 0, 1:
#     for y in 0, 1:
#         for w in 0, 1:
#             for z in 0, 1:
#                 f = (not (w <= (x == y))) and (z <= x)
#                 if f:
#                     print(x, y, w, z)

def to_sys(n, o):
    res = ''
    while n > 0:
        res = str(n % o) + res
        n //= o
    return res

#5
# for n in range(1000):
#     n4 = to_sys(n, 4)
#     if n % 4 == 0:
#         n4 = '2' + n4 + '03'
#     else:
#         n4 += to_sys((n % 4) * 5, 4)
#     r = int(n4, 4)
#     if r <= 567:
#         print(n)

#6
# from turtle import *
# k = 20
# pu()
# goto(-20 * k, 0)
# pd()
# tracer(0)
# fd(25 * k)
# right(45)
# fd(50 * k)
# pu()
# bk(50 * k)
# right(45)
# fd(15 * k)
# left(90)
# fd(30 * k)
# pd()
# right(180)
# fd(60 * k)
# bk(5 * k)
# right(90)
# fd(31 * k)
# pu()
# for x in range(-50, 50):
#     for y in range(-50, 50):
#         goto(x * k, y * k)
#         dot(3)
# done()

#9
# f = open('files/9_18594.txt')
# c = 0
# for line in f:
#     arr = [int(x) for x in line.split()]
#     ch = [x for x in arr if x % 2 == 0]
#     nch = [x for x in arr if x % 2 == 1]
#     m = min(arr)
#     if len(ch) == len(nch) and m**2 <= sum(arr) - m:
#         c += 1
# print(c)

#10
# l = '>' + 10 * '3' + 10 * '5' + 10 * '7'
# while '>3' in l or '>5' in l or '>7' in l:
#     if '>3' in l:
#         l = l.replace('>3', '55>', 1)
#     if '>5' in l:
#         l = l.replace('>5', '5>3', 1)
#     if '>7' in l:
#         l = l.replace('>7', '3>5', 1)
# print(l)
# print(sum([int(x) for x in l if x != '>']))

#13
# from ipaddress import *
# net = ip_network('222.121.128.0/255.255.224.0', False)
# c = 0
# for ip in net:
#     s = f'{ip:b}'
#     if s[-1] == s[-2]:
#         c += 1
# print(c)

#14
# alf = '0123456789ABCDEFGHIJKLMNO'
# for x in range(25):
#     ax = alf[x]
#     n = int(f'A4{ax}7F2', 25) + int(f'N{ax}G5{ax}H', 25) + int(f'74{ax}M26', 25)
#     if n % 24 == 0:
#         print(n // 24)

#22
durations = [6, 2, 5, 4, 7, 6, 3, 5, 7, 6, 9, 11]
deps = [[0], [0], [1, 2], [1], [3], [4], [4, 5], [6], [0], [0], [9], [10]]
passed = [0] * 12
end_time = [-1] * 12
ended = [False] * 12
ticks = 0
res = 0

while not all(ended):
    ticks += 1
    executing = 0
    for p in range(12):
        if not ended[p]:
            can_tick = True
            for d in deps[p]:
                if d != 0 and not ended[d - 1] or ticks == end_time[d - 1]:
                    can_tick = False
                    break
            if can_tick:
                executing += 1
                passed[p] += 1
                if passed[p] >= durations[p]:
                    ended[p] = True
                    end_time[p] = ticks
    if executing == 4:
        res += 1
print(res)

#23
# def f(s, e, h30 = False, h60 = False):
#     if h30 and h60:
#         return 0
#     if s == e:
#         return h30 or h60
#     if s > e:
#         return 0
#     h3, h6 = s == 30, s == 60
#     return f(s + 1, e, h3 or h30, h6 or h60) +  f(s * 2, e, h3 or h30, h6 or h60) +  f(s * 3, e, h3 or h30, h6 or h60)
#
# print(f(10, 70))

#24
# f = open(r"C:\Users\Ivan\Downloads\24_18239.txt")
# s = f.read()
# minuses = []
# max_length = 0
#
# for i in range(len(s)):
#     if s[i] == '-':
#         minuses.append(i)
#
# def check_slice(i):
#     global max_length
#     for j in range(i + 1, len(minuses)):
#         slice = s[minuses[i]:minuses[j]]
#         if len(slice) > max_length and slice.count('-') > 10:
#             while slice[-1] == '-':
#                 slice = slice[:-1]
#             if eval(slice) > -20_000:
#                 max_length = len(slice)
#             else:
#                 break
#
# for i in range(len(minuses) - 1):
#     check_slice(i)
#     check_slice(i + 1)
# print(max_length)

# f = open(r"C:\Users\Ivan\Downloads\26_18492 (1).txt")
# f.readline()
# timeline = [[] for _ in range(1440)]
# for line in f:
#     n, s, e = [int(x) for x in line.split()]
#     for i in range(s, e):
#         timeline[i].append(n)
# mnot = max([len(a) for a in timeline])
# nop = 0
# current_pick_length = 0
# picks = [[]]
#
# for i in range(len(timeline)):
#     if len(timeline[i]) == mnot:
#         current_pick_length += 1
#         for train_n in timeline[i]:
#             if train_n not in picks[-1]:
#                 picks[-1].append(train_n)
#
#     elif current_pick_length > 0:
#         picks.append([])
#         nop += 1
#         current_pick_length = 0
# picks = picks[:-1]
# print(len(picks))
# for pick in picks:
#     if len(pick) == 555:
#         print(sum(pick))
