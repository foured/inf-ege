# with open(r"C:\Users\Ivan\Desktop\Информатика\17\17_17636.txt", 'r') as file:
#     nums = [int(n) for n in file]
#     m3 = max([n for n in nums if str(n)[-1] == '3' and len(str(abs(n))) == 3])
#     arr = []
#     for i in range(0, len(nums) - 2):
#         a, b, c = nums[i], nums[i + 1], nums[i + 2]
#         s = a + b + c
#         if s < m3 and ((str(a)[-1] == '3' and len(str(abs(a))) == 3) or (str(b)[-1] == '3' and len(str(abs(b))) == 3) or (str(c)[-1] == '3' and len(str(abs(c))) == 3)):
#             arr.append(s)
#     print(len(arr))
#     print(max(arr))

file = open(r"C:\Users\Ivan\Downloads\17 (2).txt")
arr = [int(x) for x in file.readlines()]
m7 = abs(min([x for x in arr if abs(x) % 10 == 7]))
r = []
for i in range(0, len(arr) - 2):
    n1, n2, n3 = arr[i], arr[i + 1], arr[i + 2]
    if (len(str(abs(n1))) == 5 or len(str(abs(n2))) == 5 or len(str(abs(n3))) == 5) and abs(n1 * n2 * n3) % m7 == 0:
        r.append(n1 * n2 * n3)
print(r)