n = int(input("Nhập số số nguyên: "))
nums = list(map(int,input(f"Nhập {n} số nguyên: ").strip().split()))
nums.sort()
print("Dãy tăng dần là:",*nums)
for i in range(len(nums)):
    if nums[i] % 2 == 0: nums[i] -= 3
    else: nums[i] += 5
nums.sort(reverse=True)
print("Dãy giảm dần là:",*nums)