n = int(input("Nhập số số nguyên dương: "))
k = list(map(int, input(f"Nhập {n} số nguyên dương: ").strip().split()))
def sum_digit(num):
    while num >= 10:
        num = sum(int(digit) for digit in str(num))
    return num
codes = [sum_digit(num) for num in k]
print(f"Mã số là:", *codes)

from collections import Counter
count = Counter(codes)
max_freq = max(count.values())
most_freq = min([p for p, q in count.items() if q == max_freq])

ans = [str(num) for num, code in zip(k , codes) if code == most_freq]
print("Các số cùng mã nhiều nhất:","; ".join(ans))