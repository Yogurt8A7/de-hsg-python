n = int(input("Nhập số số nguyên dương: "))
nums = list(map(int, input(f"Nhập {n} số nguyên dương: ").strip().split()))
primes = [num for num in nums if num > 1 and all(num%i!=0 for i in range(2,int(num**0.5)+1))]
double_primes = [prime for prime in primes if all(sum(int(digit) for digit in str(prime))%i!=0 for i in range(2,int(sum(int(digit) for digit in str(prime))**0.5)+1))]
def nearest_prime(num):
    num1 = num
    num2 = num
    while True:
        num1 +=1
        num2 -=1
        if all(num1%i!=0 for i in range(2,int(num1**0.5)+1)):
            if all(num2%i!=0 for i in range(2,int(num2**0.5)+1)):
                if num - num2 == num1 - num:
                    return num1
                elif num - num2 < num1 - num:
                    return num2 
            else:
                return num1
        else:
            if all(num2%i!=0 for i in range(2,int(num2**0.5)+1)):
                return num2
print("Các số nguyên tố của dãy là:", *primes)
print("Các số song tố là:",*double_primes)
print("Các số nguyên tố gần nhất:",*[nearest_prime(num) for num in nums])