from sympy import isprime
n = int(input("Nhập số tự nhiên n (n > 2): "))
prime_sum = 0   
primes = []      
for i in range(1, n):  
    if isprime(i):
        prime_sum += i
        primes.append(i)
ans = max(primes) if primes else None 
print(f"Số chữ số của {n}: {len(str(n))}")
print(f"Tổng các chữ số của {n}: {sum(int(ch) for ch in str(n))}")
print(f"Tổng các số nguyên tố nhỏ hơn {n}: {prime_sum}")
l = n-1 ; u = n+1
while True:
    if l >= 2 and isprime(l):
        print(l)
        break
    if isprime(u):
        print(u)
        break
    l-=1
    u+=1
