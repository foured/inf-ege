# f = open('24_demo.txt')
# s = f.read()
# s = s.replace('Y', ';').replace('Z', ';')
# print(max([len(x) for x in s.split(';')]))
from webbrowser import Error

# f = open(r"C:\Users\Ivan\Downloads\24_17756.txt")
# s = f.read().replace('++', '+;+').replace('**', '*;*').replace('*+', '*;+').replace('+*', '+;*')
# s = s.replace('++', '+;+').replace('**', '*;*').replace('*+', '*;+').replace('+*', '+;*')
# print(max([len(x) for x in s.split(';')]))

# f = open(r"C:\Users\Ivan\Downloads\24_16388.txt")
# s = f.read()
# cc = 1
# m = -1
# for i in range(0, len(s) - 1):
#     if s[i] == 'K' and s[i + 1] == 'L':
#         cc += 1
#     elif s[i] == 'L' and s[i + 1] == 'M':
#         cc += 1
#     elif s[i] == 'M' and s[i + 1] == 'N':
#         cc += 1
#     elif s[i] == 'N' and s[i + 1] == 'K':
#         cc += 1
#     else:
#         m = max(m, cc)
#         cc = 1
# print(m)

# f = open(r"C:\Users\Ivan\Downloads\24_16333.txt")
# s = f.read().strip().replace('R', 'Q').replace('W', 'Q').replace('2', '1').replace('4', '1')
# s = s.replace('QQ', 'Q;Q').replace('11', '1;1')
# s = s.replace('QQ', 'Q;Q').replace('11', '1;1')
# print(max([len(x) for x in s.split(';')]))

#================================================================================================= 14647
# f = open(r"C:\Users\Ivan\Downloads\24.14_14647.txt")
# s = f.read().strip()
# idxs = []
# start = 0
# m = -1
# for i in range(len(s)):
#     if s[i] in 'XY':
#         idxs.append(i)
#         if len(idxs) > 2:
#             start = idxs[0] + 1
#             del idxs[0]
#     if len(idxs) == 2 and s[idxs[0]] != s[idxs[1]]:
#         m = max(m, i - start + 1)
# print(m)

# f = open(r"C:\Users\Ivan\Downloads\24.13_14643.txt")
# s = f.read().strip().replace('AXMM', 'AXM;M')
# print(max([len(x) for x in s.split(';')]) + 2)

# file = open(r"C:\Users\Ivan\Downloads\24_18186.txt")
# s = file.read().strip()
# l = -1
# max_l = 0
# for i in range(0, len(s) - 2):
#     c1, c2, c3 = s[i], s[i + 1], s[i + 2]
#     if c1 in 'BCDFGH' and c2 in 'BCDFGH' and c3 in 'AE':
#         if l != -1:
#             max_l = max(max_l, i + 2 - l + 1)
#         l = i
# print(max_l)

# file = open(r"C:\Users\Ivan\Downloads\24_17878 (1).txt")
# s = file.read().strip().replace('*', '-').replace('7', '6').replace('8', '6').replace('9', '6')
# s = s.replace('--', '-;-').replace('-00', '-0;-0').replace('-06', '-0;6')
# print(sorted([len(y.strip('-')) for y in s.split(';')]))

# file = open(r"C:\Users\Ivan\Downloads\24_18147.txt")
# s = file.read().strip().replace('*', ';').replace('++', '+;+')
# print(max([eval(y) for y in [x.strip('+') for x in s.split(';')] if y.count('+') >= 1]))

# file = open(r"C:\Users\Ivan\Downloads\24_17756 (2).txt")
# s = file.read().strip().replace('*', '+').replace('++', '+;+').replace('++', '+;+')
# print(max([len(x) for x in s.split(';')]))

# file = open(r"C:\Users\Ivan\Downloads\24_17685.txt")
# s = (file.read().strip()
#       .replace('++', '+;+').replace('+*', '+;*').replace('**', '*;*').replace('*+', '*;+'))
# ml = -1
# for l in s.split(';'):
#     if len(l) < ml:
#         continue
#     for i in range(0, len(l) - 1):
#         for j in range(i + 1, len(l)):
#             cl = l[i:j + 1].strip('+').strip('*')
#             if len(cl) >= 2 and cl[0] == '0' and cl[1] not in '*+':
#                 continue
#             if (cl.count('*') + cl.count('+') >= 1) and (eval(cl) == 0):
#                 ml = max(len(cl), ml)
# print(ml)

# file = open(r"C:\Users\Ivan\Downloads\24.txt")
# s = file.read().strip()
# L = []
# O = []
# V = []
# E = []
# for i in range(len(s)):
#     if s[i] == 'L': L.append(i)
#     if s[i] == 'O': O.append(i)
#     if s[i] == 'V': V.append(i)
#     if s[i] == 'E': E.append(i)
#
# si = max(l for l in L if l < min(O))
# print(si)
#
# res = 10**8
# for l in L:
#     if l >= si:
#         os = [x for x in O if x > l]
#         os.append(10**6)
#         o = min(os)
#         vs = [x for x in V if x > o]
#         vs.append(10**6)
#         v = min(vs)
#         es = [x for x in E if x > v]
#         es.append(10**6)
#         e = min(es)
#         res = min(res, (e - l + 1))
# print(res)

# f=open(r"C:\Users\Ivan\Downloads\24.txt").readline().strip()
# #f='REVVLAAORRVEARRLBOLRVER'
# io=f.index('O')
# Lmin=max([x for x in range(len(f)) if x<io and f[x]=="L"])
# L=[x for x in range(Lmin,len(f)) if f[x]=='L']
# O=[x for x in range(Lmin,len(f)) if f[x]=='O']
# V=[x for x in range(Lmin,len(f)) if f[x]=='V']
# E=[x for x in range(Lmin,len(f)) if f[x]=='E']
# res = 10**12
# for l in L:
#     os = [x for x in O if x > l]
#     os.append(10**12)
#     o = min(os)
#     vs = [x for x in V if x > o]
#     vs.append(10**12)
#     v = min(vs)
#
#
#     es = [x for x in E if x > v]
#     es.append(10**12)
#     e = min(es)
#     res = min(res, (e - l + 1))
# print(res,f[l],f[o],f[v],f[e])

# f = open(r"C:\Users\Ivan\Downloads\24-300.txt")
# s = f.read().strip().replace('++', '+;+').replace('**', '*;*')\
#      .replace('+*', '+;*').replace('*+', '*;+')
# m = -1
# for v in s.split(';'):
#     if len(v) > m:
#         for i in range(len(v) - 1):
#             for j in range(i + 1, len(v)):
#                 cl = v[i:j+1].strip('+').strip('*')
#                 if ('+' in cl or '*' in cl) and all('0'+x != cl[0:2] for x in '0123456789') and all(y+'0'+x not in cl for x in '0123456789' for y in '+*'):
#                     if eval(cl) == 0:
#                         m = max(m, len(cl))
# print(m)

# from re import *
# f = open(r"C:\Users\Ivan\Downloads\k7a-1.txt")
# s = f.read()
# pattern = r'[ABC]+'
# print(max([len(x) for x in findall(pattern, s)]))

# from re import *
# f = open(r"C:\Users\Ivan\Downloads\k7a-4.txt")
# s = f.read()
# pattern = r'[^D]+'
# print(max([len(x) for x in findall(pattern, s)]))

# from re import *
# f = open(r"C:\Users\Ivan\Downloads\24-196.txt").read()
# pattern = r'(?:ZX|ZY)+'
# print(max([len(x) for x in findall(pattern, f)]) // 2)

# from re import *
# f = open(r"C:\Users\Ivan\Downloads\24-212.txt").read()
# pattern = r'(?:[BCD][AO])+'
# print(max(len(x) for x in findall(pattern, f)) // 2)

# from re import *
# f = open(r"C:\Users\Ivan\Downloads\24-204.txt").read()
# pattern = r'(?:AA|CC)+'
# m = []
# for i in range(len(f)):
#     c = search(pattern, f)
#     if c:
#         m.append(len(c[0]))
#         f = f[1:]
# print(max(m) // 2)

# from re import *
# f = open(r"C:\Users\Ivan\Downloads\24-215.txt").read()
# pattern = r'(?:[123][ABC][123])+'
# m = 0
# for i in range(len(f)):
#     c = search(pattern, f)
#     if c:
#         m = max(m, len(c[0]))
#         f = f[c.end() - 1:]
# print(m // 3)

# from re import *
# f = open(r"C:\Users\Ivan\Downloads\24-298.txt").read()
# num = r'(?:[789][0789]*)'
# pattern = rf'{num}(?:[-*]{num})+'
# print(max(len(x) for x in findall(pattern, f)))

# from re import *
# f = open(r"C:\Users\Ivan\Downloads\24-310.txt").read()
# num = r'(?:[12][012]*|0)'
# pattern = rf'{num}(?:[+*]{num})*'
# res = sorted(findall(pattern, f), reverse=True, key=len)
# print(len(res[0]), res[0])

# from re import *
# f = open(r"C:\Users\Ivan\Downloads\24-299.txt").read()
# num = r'(?:[1-9][0-9]*|0)'
# pattern = rf'{num}(?:[+*]{num})*'
# print(max([len(x) for x in findall(pattern, f) if eval(x) == 0]))
# mul = rf'(?:(?:{num}[*])*0(?:[*]{num})*)'
# pattern = rf'{mul}(?:[+]{mul})*'
# res = sorted(findall(pattern, f), reverse=True, key=len)
# print(len(res[0]), res[0])

# from re import *
# f = open(r"C:\Users\Ivan\Downloads\24-305.txt").read()
# num = r'(?:[1-9][0-9]*|0)'
# pattern = rf'AF{num}(?:[+*]{num})*'
# print(max(len(x) for x in findall(pattern, f)))

from re import *
f = open(r"C:\Users\Ivan\Downloads\24_19970.txt").read()
num = r'(?:[1-9][0-9]*[05]|0|5)'
pattern = rf'{num}(?:[+*]{num})*'
print(max(len(x) for x in findall(pattern, f)))
