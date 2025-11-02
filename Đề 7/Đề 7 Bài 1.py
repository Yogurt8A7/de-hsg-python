n = int(input("Nhập số nguyên n: "))
S = 0
for i in range(1, n+1):
    S -= 1 / (i**2 + 1) if i % 2 == 0 else 0 
    S += 1 / (i**2 + 1) if i % 2 != 0 else 0
def x(n):
    total = 0
    x = 1
    while total <= n:
        total += x/(x+1)
        x+=1
    return x - 2
print("S =",round(S,4))
print("x =",x(n))