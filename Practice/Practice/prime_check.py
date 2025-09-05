# Check if number is prime

def check(n):
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


num = int(input("Enter the number you want to check for prime: "))
prime_num = check(num)

if num >=2 and prime_num:
    print(f"Yes {num} is a prime number.")
else:
    print(f"No {num} is not a prime number.")

