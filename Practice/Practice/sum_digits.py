# Sum of digits of a number

def digit_Sum(n):
    sum = 0
    while n > 0:
        x = n % 10
        sum += x
        n //= 10
    return sum

num = int(input("Enter the number: "))

print(f"The sum of digits of a number: {digit_Sum(num)}")