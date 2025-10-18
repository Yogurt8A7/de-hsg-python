n = int(input("Nhập số tự nhiên n: "))
nums = list(map(int, input(f"Nhập {n} số nguyên < 5: ").strip().split()))
c1 = nums.count(1)
c2 = nums.count(2)
c3 = nums.count(3)
c4 = nums.count(4)

rooms = c4

pair_3_1 = min(c3, c1)
rooms += pair_3_1
c3 -= pair_3_1
c1 -= pair_3_1
rooms += c3

pair_2_2 = c2 // 2
c2 = c2 % 2
rooms += pair_2_2

if c2 == 1:
    if c1 >= 2:
        c1 -= 2
        rooms += 1
    else:
        rooms += 1
        c1 = 0
rooms += (c1 + 3) // 4
print(f"Số phòng ít nhất là: {rooms}")