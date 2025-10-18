from collections import Counter
n = int(input("Nhập số lượng phần tử trong dãy số: "))
nums = list(map(int, input(f"Nhập {n} số nguyên: ").strip().split()))
k = int(input("Nhập số k: "))

nums.sort()
greater_count_k = []
count = Counter(nums)
for i, j in count.items():
    if j >= k:
        greater_count_k.append(i)
print("Dãy tăng dần là:",*nums)
if greater_count_k:
    print(f"Các số xuất hiện {k} lần trở lên là:", *greater_count_k)
else:
    print("KHONG")