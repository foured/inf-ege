#19257
# A  = open(r'files/n27/19257_A.txt')
# B  = open(r'files/n27/19257_B.txt')
#
# clA = [[], []]
# clB = [[], [], []]
#
# for line in A:
#     x, y = [float(r) for r in line.split()]
#     if y > 8:
#         clA[0].append([x, y])
#     else:
#         clA[1].append([x, y])
#
# for line in B:
#     x, y = [float(r) for r in line.split()]
#     if x < 0:
#         clB[0].append([x, y])
#     elif y < 7:
#         clB[1].append([x, y])
#     else:
#         clB[2].append([x, y])
#
# def findDist(p1, p2):
#     x1, y1, x2, y2 = *p1, *p2
#     return ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5
#
# def center(c):
#     s = []
#     for p in c:
#         s.append([sum([findDist(p, p1) for p1 in c]), p])
#     return min(s)[1]
#
# Apx = center(clA[0])[0]
# Apx += center(clA[1])[0]
# Apx /= 2
# Apx *= 10_000
# Apy = center(clA[0])[1]
# Apy += center(clA[1])[1]
# Apy /= 2
# Apy *= 10_000
# print(abs(int(Apx)), abs(int(Apy)))
#
# Apx = center(clB[0])[0]
# Apx += center(clB[1])[0]
# Apx += center(clB[2])[0]
# Apx /= 3
# Apx *= 10_000
# Apy = center(clB[0])[1]
# Apy += center(clB[1])[1]
# Apy += center(clB[2])[1]
# Apy /= 3
# Apy *= 10_000
# print(abs(int(Apx)), abs(int(Apy)))

#18678
# A = open(r'files/n27/27A_18678.txt')
# B = open(r'files/n27/27B_18678.txt')
#
# clA = [[], []]
# clB = [[], [], []]
#
# for line in A:
#     x, y = [float(r) for r in line.split()]
#     if y < 2.5:
#         clA[0].append([x, y])
#     elif 1 < x < 6:
#         clA[1].append([x, y])
#
# k = -(11/4)
# # 10 = -(11/4) * 1 + b
# b = 10 + 11/4
# for line in B:
#     x, y = [float(r) for r in line.split()]
#     if y < k * x + b and y > -1.5:
#         clB[0].append([x, y])
#     elif 3 <= x <= 6.5 and 1.5 <= y <= 7:
#         clB[1].append([x, y])
#     elif not (y > 9 and x > 8) and x > 4:
#         clB[2].append([x, y])
#
# def findDist(p1, p2):
#     x1, y1, x2, y2 = *p1, *p2
#     return ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5
#
# def center(c):
#     s = []
#     for p in c:
#         s.append([sum([findDist(p, p1) for p1 in c]), p])
#     return min(s)[1]
#
# Apx = center(clA[0])[0] + center(clA[1])[0]
# Apx *= 50_000
# Apy = center(clA[0])[1] + center(clA[1])[1]
# Apy *= 50_000
# print(abs(int(Apx)), abs(int(Apy)))
#
# Apx = center(clB[0])[0] + center(clB[1])[0] + center(clB[2])[0]
# Apx *= 100_000 / 3
# Apy = center(clB[0])[1] + center(clB[1])[1] + center(clB[2])[1]
# Apy *= 100_000 / 3
# print(abs(int(Apx)), abs(int(Apy)))

fa = open(r"C:\Users\Ivan\Downloads\27-p00a.txt")
fb = open(r"C:\Users\Ivan\Downloads\27-p00b.txt")

clA = [[], []]
clB = [[], [], []]

for line in fa:
    x, y = [float(p) for p in line.split()]
    if y > 3:
        clA[0].append([x, y])
    else:
        clA[1].append([x, y])

#7 3.5
for line in fb:
    x, y = [float(p) for p in line.split()]
    if y > 7:
        clB[0].append([x, y])
    elif y > 3.5:
        clB[1].append([x, y])
    else:
        clB[2].append([x, y])

def findDist(p1, p2):
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5

def findCenter(claster):
    s = []
    for p1 in claster:
        s.append([sum([findDist(p1, p2) for p2 in claster]), p1])
    return min(s)[1]

pxA = (findCenter(clA[0])[0] + findCenter(clA[1])[0]) * 5000
pyA = (findCenter(clA[0])[1] + findCenter(clA[1])[1]) * 5000
print(pxA)
print(pyA)
pxB = (findCenter(clB[0])[0] + findCenter(clB[1])[0] + findCenter(clB[2])[0]) * 10000 / 3
pyB = (findCenter(clB[0])[1] + findCenter(clB[1])[1] + findCenter(clB[2])[1]) * 10000 / 3
print(pxB)
print(pyB)