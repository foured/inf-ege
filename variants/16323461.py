#---2
# print('y x w z')
# for x in 0, 1:
#     for y in 0, 1:
#         for w in 0, 1:
#             for z in 0, 1:
#                 f = ((y <= w) == (x <= (not z))) and (x or w)
#                 if f == 1 and w == 0:
#                     print(y, x, w, z)

#---5
# m = 0
# for n in range(1, 101):
#     bn = bin(n)[2::]
#     bn = bn[::-1]
#     r = int(bn, 2)
#     if r == 13:
#         m = max(m, n)
# print(m)

#---6
# count = 0
# for x in range(1, 10):
#     for y in range(1, 10):
#         if (y > x * 3 ** 0.5) or (y < (x - 6) * 3 ** 0.5) or (y > (36 - 9)**(1/2)):
#             count += 1
# print(count)

#---8
# from itertools import product
# products = product('СВЕТА', repeat=5)
# count=0
# for i in products:
#     p = ''.join(i)
#     if p.count('С') != 0:
#         count+=1
# print(count)

#---9
# with open(r"C:\Users\Ivan\Desktop\Информатика\9\09.csv") as file:
#     count = 0
#     for line in file:
#         arr = [int(x) for x in line.split(";")]
#         mi = min(arr)
#         ma = max(arr)
#         if len(set(arr)) == len(arr) and ((mi + ma) / 2) < ((sum(arr) - mi - ma) / 4):
#             count += 1
#     print(count)

#---12
# p = '>' + '1'* 11 + '2'* 12 + '3'* 30
# while ('>1' in p) or ('>2' in p) or ('>3' in p):
#     if '>1' in p:
#         p = p.replace('>1', '22>', 1)
#     if '>2' in p:
#         p = p.replace('>2', '2>', 1)
#     if '>3' in p:
#         p = p.replace('>3', '1>', 1)
# p = p.replace('>', '')
# s = sum([int(x) for x in list(p)])
# print(s)

#---13
# from ipaddress import *
# for mask in range(0, 33):
#     ip = ip_address('119.83.200.27')
#     net = ip_network(f'{ip}/{mask}', False)
#     net_ip = ip_address('119.83.192.0')
#     if net.network_address == net_ip:
#         print(mask)

#---14
# n = 9**11 * 3**20 - 3**9 - 27
# count = 0
# while n > 0:
#     if n % 3 == 2:
#         count += 1
#     n //= 3
# print(count)

#---15
# def f(x, y, a):
#     return (x > a) or (y > x) or (2*y + x < 110)
# m = 0
# for a in range(0, 1000):
#     if all(f(x, y, a) for x in range(0, 1000) for y in range(0, 1000)):
#         m = max(m, a)
#
# print(m)

#---16
# def f(n):
#     if n <= 1:
#         return 0
#     if n % 2 == 0:
#         return n / 2 + f(n - 1) + 2
#     return f(n - 1) + 3 * n**2
# print(f(49))

#---17
# with open(r"C:\Users\Ivan\Downloads\17 (1).txt") as file:
#     arr = [int(x) for x in file]
#     al = len(arr)
#     n = 0
#     ms = -1
#     for i in range(0, al):
#         for j in range(i + 1, al):
#             n1 = arr[i]
#             n2 = arr[j]
#             if (n1 * n2) % 26 == 0:
#                 n += 1
#                 ms = max(ms, n1 + n2)
#     print(n)
#     print(ms)

#---19-21
def f(s, t, c):
    if s >= 151:
        return t % 2 == c % 2
    if t >= c:
        return 0

    h = []
    fr = f(s + 1, t + 1, c)
    if (s + 1) % 3 != 0:
        h.append(fr)
    fr = f(s + 2, t + 1, c)
    if (s + 2) % 3 != 0:
        h.append(fr)
    fr = f(s * 2, t + 1, c)
    if (s * 2) % 3 != 0:
        h.append(fr)

    return any(h) if (t + 1) % 2 == c % 2 else all(h)

print('19: ', [s for s in range(1, 149) if s % 3 != 0 and f(s, 0, 1) == 0 and f(s, 0, 2)])
print('20: ', [s for s in range(1, 149) if s % 3 != 0 and f(s, 0, 1) == 0 and f(s, 0, 3)])
print('20: ', [s for s in range(1, 149) if s % 3 != 0 and f(s, 0, 2) == 0 and f(s, 0, 4)])