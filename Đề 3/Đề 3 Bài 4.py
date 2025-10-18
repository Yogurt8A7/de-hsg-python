n = int(input("Nhập số thanh gỗ: ").strip())
lengths = list(map(int, input("Nhập độ dài các thanh gỗ: ").strip().split()))
k = int(input("Nhạp số nguyên dương k: ").strip())

min_lnt = min(lengths)
total_cuts = 0
for l in lengths:
    total_cuts += (l - min_lnt)
print("Tổng số mét gỗ cắt bỏ là:",total_cuts)

l, r = 0, max(lengths)
h_max = 0
while l <= r:
    mid= (l + r) // 2
    total_cut = sum(max(0, l - mid) for l in lengths)

    if total_cut >= k:
        h_max = mid
        l = mid + 1
    else:
        r = mid - 1
print("Độ dài lớn nhất là:", h_max)