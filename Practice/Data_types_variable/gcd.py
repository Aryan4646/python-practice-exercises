 # A function that finds the greatest common divisor (GCD) of two numbers
def gcd(a, b):
    gcd = 1
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            gcd = i  
    return gcd

def gcd_euc(a,b):
    while b != 0:
        a, b = b, a % b
    return a

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print(f"Greatest common divisor: {gcd(num1,num2)}")
print(f"Greatest common divisor using euclidean algorithm: {gcd_euc(num1,num2)}")