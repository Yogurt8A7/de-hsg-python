import math
a, b, c = map(int, input("Nhập ba số nguyên a, b, c: ").strip().split())
lst = [a, b, c]
print(f"Số lớn nhất là:",max(lst))
print(f"UCLN({a}, {b}, {c}) = {math.gcd(math.gcd(a,b), c)}")
if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
    print(f"({a}, {b}, {c}) là bộ ba số Pytago")