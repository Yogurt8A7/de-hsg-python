S = input("Nhập chuỗi S: ")
import re
a = ""
for ch in S:
    if ch.isdigit():
        a+=ch
b = "KHONG"
for i in range(len(a) - 1, -1, -1):
    if a[i] in ('0','5'):
        b = a[:i+1]
nums = re.findall(r'\d+', S)
T = sum(int(n) for n in nums)
print(f"a = {a}, b = {b}, T = {T}")