from fractions import Fraction

m = int(input("Nhập số nguyên dương m: "))
n = int(input("Nhập số nguyên dương n: "))
if m < n:
    a = 0
    for i in range(m, n+1):   a += (i if i % 2 != 0 else 0)
    print("Tổng các số lẻ là:",a)
    print("Phân số tổi giản là:", Fraction(m, n))
    found = False
    for x in range(1, m+1):
        for y in range(1, m+1):
            if x + y == m and x * y == n: 
                print(f"x = {x}\ny = {y}")
                found = True
                break
        if found:
            break
    if not found:
        print("KHONG")      
else:
    print("Đầu vào không hợp lệ")