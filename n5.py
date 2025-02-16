# def to_sys(num, sys):
#     res = ''
#     while num > 0:
#         res = str(num % sys) + res
#         num //= sys
#     return res
#
# m = 0
# for n in range(13):
#     bin_n = to_sys(n, 2)
#     if n % 2 == 0:
#         bin_n = '10' + bin_n
#     else:
#         bin_n = '1' + bin_n + '01'
#     r = int(bin_n, 2)
#     m = max(m, r)
# print(m)


def to_sys(n, osn):
    res = ''
    while n > 0:
        res = str(n % osn) + res
        n //= osn
    return res

# mr = 10**8
# for n in range(1, 10_000):
#     n6 = to_sys(n, 6)
#     if n % 3 == 0:
#         n6 += n6[:2]
#     else:
#         n6 += to_sys((n % 3) * 10, 6)
#     r = int(n6, 6)
#     if r > 680:
#         mr = min(mr, r)
# print(mr)

# for n in range(1, 1000):
#     bn = bin(n)[2:]
#     if bn.count('1') % 2 == 0:
#         bn = '10' + bn[2:] + '0'
#     else:
#         bn = '11' + bn[2:] + '1'
#     r = int(bn, 2)
#     if r > 171:
#         print(n)
#         break

# m = 10**8
# for n in range(1, 1000):
#     bn = bin(n)[2:]
#     o = bn.count('1') % 2
#     bn += str(o)
#     o = bn.count('1') % 2
#     bn += str(o)
#     r = int(bn, 2)
#     if r > 123:
#         m = min(m, r)
# print(m)