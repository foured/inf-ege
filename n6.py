# count = 0
# for x in range(-20, 20):
#     for y in range(-20, 20):
#         if 0 < x < 75**0.5 and y > (x / 3**0.5) and y < (x / 3**0.5 + 10):
#             count += 1
# print(count)

# count = 0
# for x in range(1, 9):
#     for y in range(1, 9):
#         if (y < x / 3 ** 0.5) or (y > -x / 3 ** 0.5 + 9):
#             count += 1
# print(count)

# from turtle import *
# left(90)
# tracer(0)
# k = 20
# right(90)
# for i in range(3):
#     right(45)
#     fd(10 * k)
#     right(45)
# right(315)
# fd(10 * k)
# for i in range(2):
#     right(90)
#     fd(10 * k)
# pu()
# for x in range(-30, 30):
#     for y in range(-30, 30):
#         goto(x * k, y * k)
#         dot(4)
# done()

# count = 0
# for x in range(-100, 100):
#     for y in range(-100, 100):
#         if y < x + (10 * 2**0.5) and y > x - (10 * 2**0.5) and y < -x and y > -x - (10 * 2**0.5):
#             count += 1
# print(count)

# from turtle import *
# k = 15
# tracer(0)
# left(90)
# for i in range(4):
#     fd(16 * k)
#     left(90)
#     fd(20 * k)
#     left(90)
# pu()
# fd(4 * k)
# left(90)
# fd(8 * k)
# right(180)
# pd()
# for i in range(3):
#     fd(35 * k)
#     left(90)
#     fd(6 * k)
#     left(90)
# pu()
# for x in range(-50, 50):
#     for y in range(-50, 50):
#         goto(x * k, y * k)
#         dot(3)
# done()

from turtle import *
k = 30
tracer(0)
screensize(5000, 5000)
for i in range(2):
    fd(6 * k)
    rt(90)
    fd(12 * k)
    rt(90)
pu()
fd(1 * k)
rt(90)
fd(3 * k)
lt(90)
pd()
for i in range(2):
    fd(77 * k)
    rt(90)
    fd(45 * k)
    rt(90)
pu()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * k, y * k)
        dot(3)
done()