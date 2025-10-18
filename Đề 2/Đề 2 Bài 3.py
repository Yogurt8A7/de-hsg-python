S = input("Nhập xâu S:")
S1 = ""
S2 = ""
for ch in S:
    if not ch.isdigit():
        S1 += ch
for ch in S1:
    if not S2 or ch != S2[-1]:
        S2+=ch

print("Tổng các chữ số là",sum(int(ch) for ch in S if ch.isdigit()))
print("S1 =", S1)
print("S2 =", S2)
