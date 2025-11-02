n = int(input("Nhập số km đi taxi: ").strip())

price = 0
for i in range(1, n+1):
    if 1 == i:
        price += 10000
    elif 2 <= i <= 10:
        price += 9000
    else:
        price += 8000
if n > 50:
    price *= 0.9
print("Số tiền đi taxi là:", int(price))