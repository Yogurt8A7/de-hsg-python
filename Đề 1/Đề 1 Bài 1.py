m = int(input("Nhập số con: "))
n = int(input("Nhập số chân: "))
if n % 2 != 0 or n > 2*m or n >4*m: print("KHONG")
else:
    so_cho = n // 2 - m
    so_ga = m - so_cho
    print(f"Ga: {so_ga}, Cho: {so_cho}")
    