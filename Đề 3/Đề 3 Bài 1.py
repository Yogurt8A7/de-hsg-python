n = int(input("Nhập số tự nhiên n: "))
k = 0
uoc = 0
digit = []
for i in str(n):
    k +=1
    digit.append(int(i))
for i in range(1,n+1): 
    uoc+=1 if n%i == 0 else 0
CSLN = max(digit)
SLN = ""
for _ in range(0, k):
    SLN += str(max(digit))
    digit.remove(max(digit))

print(f"{n} có {uoc} ước")
print(f"{n} có {k} chữ số")
print(f"Chữ số lớn nhất trong {n} là {CSLN}")
print(f"Số lớn nhất là {SLN}")

