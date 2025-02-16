# ml = -1
# for n in range(4, 1000):
#     l = '1' + '2' * n
#     while '12' in l or '322' in l or '222' in l:
#         if '12' in l:
#             l = l.replace('12', '2', 1)
#         if '322' in l:
#             l = l.replace('322', '21', 1)
#         if '222' in l:
#             l = l.replace('222', '3', 1)
#     ml = max(len(l), ml)
# print(ml)

s = set()
for n in range(3, 101):
    l = '7' + '6' * n
    while '766' in l or '667' in l:
        if '766' in l:
            l = l.replace('766', '67', 1)
        if '667' in l:
            l = l.replace('667', '7', 1)
    s.add(l)
print(s)