# Print all primes up to N

def isprime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

num = int(input("Enter the number upto which you want to find prime numbers: "))

for i in range(2,num+1):
    if isprime(i):
        print(i,end=" ")
