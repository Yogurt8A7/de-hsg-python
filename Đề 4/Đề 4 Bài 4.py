from math import sqrt
n = int(input("Nhập số nguyên dương n: "))

res = []
while n > 0:
    x = int(sqrt(n))
    res.append(x)
    n -= x ** 2
print("Dãy cần tìm là:", *res)