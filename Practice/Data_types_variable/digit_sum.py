# Write a function to calculate the sum of all digits of a given integer.

def sum_digit(s,n):
    if n == 0:
        return s
    else:
        return sum_digit((s+(n%10)), n//10 )

num = int(input("Enter the number: "))
s = 0
print(f"Sum of digits of {num} is equal to {sum_digit(s, num)}")