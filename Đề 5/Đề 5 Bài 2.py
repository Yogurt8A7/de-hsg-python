n = int(input("Nhập số nguyên dương n: "))
k = 0
s = 0
d = []
p = "KHONG"
for i in str(n): 
    k += 1
    s += int(i)
    d.append(int(i))
for j in range(len(str(n)) - 1, -1, -1):
    if str(n)[j] in ('0','5'):
        b = str(n)[:j+1]
print("Số chữ số của n:", k)
print("Tổng các chữ số là:",s)
print("Chữ số lớn nhất là:",max(d))
print("Số lớn nhất chia hết cho 5 là:",b)
