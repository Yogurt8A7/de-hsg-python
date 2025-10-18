a, b, c = map(int, input("Nhập ba số nguyên dương a, b, c: ").strip().split())
k = int(input("Nhập số nguyên dương k: "))
nums = []
nums.append(a)
nums.append(b)
nums.append(c)
prods = []
prods.append(a*b)
prods.append(b*c)
prods.append(c*a)
P = max(prods)
print("Số nhỏ nhất là",min(nums))
print("Số dư là", P % k)
