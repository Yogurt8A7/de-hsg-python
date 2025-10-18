n = int(input("Nhập n: "))
P = sum(int(ch) for ch in str(n))
S = 0
for i in range(2, n + 2):
    if i % 2 == 0:
        S += 1/i
    else:
        S -= 1/i
S = round(S, 4)
tong = 0
k = 0
while tong + (k + 1) * (k + 2) <= n * n:
    k += 1
    tong += k * (k + 1)
print(f"P = {P}, S = {S}, k = {k}")