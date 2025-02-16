# with open(r'D:\Python\informatics\demo_2025_9.csv') as file:
#     count = 0
#     for line in file:
#         arr = [int(x) for x in line.split(';')]
#         p3 = [x for x in arr if arr.count(x) == 3]
#         np = [x for x in arr if arr.count(x) == 1]
#
#         if len(p3) == 3 and len(np) == 3 and sum(p3)**2 > sum(np)**2:
#             count += 1
#     print(count)

# file = open('n9_12_10.txt')
# for line in file:
#     arr = [int(x) for x in line.strip().split()]
#     p2 = [x for x in arr if arr.count(x) == 2]
#     p1 = [x for x in arr if arr.count(x) == 1]
#     if len(p2) == 4 and len(p1) == 3 and arr.count(max(arr)) == 1:
#         print(sum(arr))
#         break

file = open('9_17628.txt')
c = 0
for line in file:
    arr = [int(x) for x in line.strip().split()]
    p = [x for x in arr if arr.count(x) > 1]
    np = [x for x in arr if arr.count(x) == 1]
    pr = 1
    for i in p:
        pr *= i
    if len(p) > 0 and 3 * sum(np) <= pr:
        c += 1
print(c)