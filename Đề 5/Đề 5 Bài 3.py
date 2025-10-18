import math
AB = int(input("Nhập độ dài cạnh AB: "))
AH = int(input("Nhập độ dài cạnh AH: "))
BH = round(math.sqrt((AB ** 2) - (AH ** 2)), 2)
AC = round(AH**2 / math.sqrt(AB**2 - AH**2), 2)
print("BH =", BH)
print("CH =", AC)