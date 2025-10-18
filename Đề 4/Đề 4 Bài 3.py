m, n = map(int,input("Nhập hai số nguyên dương m, n: ").strip().split())
from sympy import isprime
primes = [x for x in range(1, m) if isprime(x)]
print("Dãy 1 là:",*primes)
if isprime(m): primes.append(m)
n_sumdigit_primes = [p for p in primes if sum(int(d) for d in str(p)) == n]
print("Dãy 2 là:",*n_sumdigit_primes) if n_sumdigit_primes else print("KHONG")