a,b,c,d = map(int,input("Nhập bốn số nguyên dương a, b, c, d: ").strip().split())
from fractions import Fraction
S = Fraction(a,b)+Fraction(c,d)
Q = Fraction(a,b)/Fraction(c,d)
print("S =",S)
print("Q =",Q)