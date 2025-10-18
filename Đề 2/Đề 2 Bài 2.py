import math
from math import gcd
from fractions import Fraction

a, b = map(int, input("Nhập hai số tự nhiên a, b: ").split())

print(f"UCLN là: {gcd(a,b)}")
print(f"Phân số tối giản là: {Fraction(a,b)}")

def sqrts(a, b):
    res = []
    for n in range(a, b+1):
        x = math.isqrt(n)
        if x * x == n:
            res.append(n)
    return res

print("Các số chính phương là:", *sqrts(a, b))

def is_stairs():
    count = 0
    for n in range(a,b+1):
        s = str(n)
        for i in range(1, len(s)):
            if s[i] < s[i-1]:  
                count+=0
            else:
                count+=1
    return count

print("Số số bậc thang là:", is_stairs())
