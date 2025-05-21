# Implement exponentiation by squaring (efficient power function).

def power(num, expo):

    if expo == 0:
        return 1
    if expo % 2 == 0:
        half = power(num, expo//2)
        z = half * half
    else:
        half = power(num, expo//2)
        z = num * half * half
    return z


num = int(input("Enter the number: "))
expo = int(input("Enter the exponent: "))

print(f"{num} raise to power {expo} is equal to {power(num, expo)}")