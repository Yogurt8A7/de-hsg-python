n = int(input("Nhập số nguyên dương n: ").strip())
S = 0
sum = 0
nums = []
for i in range(1, n+1):
    S += i / (i+1)
S = round(S, 4)
i = 1
while sum+i <= n:
    nums.append(i)
    sum += i
    i +=1
x = max(nums)
print("S =", S)
print("x =", x)