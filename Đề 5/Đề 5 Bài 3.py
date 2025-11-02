import math
AB = int(input("Nhập độ dài cạnh AB: "))
AH = int(input("Nhập độ dài cạnh AH: "))
BH = math.sqrt((AB ** 2) - (AH ** 2))
CH = AH**2 / math.sqrt(AB**2 - AH**2)
print("BH =", BH:.2f)
print("CH =", CH:.2f)
