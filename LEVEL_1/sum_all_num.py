num = int(input("Enter the number: "))
sum_digit = 0
print(f"The number is {num}.")
temp = num
if temp < 0:
    temp = temp * (-1)    # negative number too because we need sum of digits
while temp > 0:
    r = temp % 10
    sum_digit += r
    temp //= 10
print(f"The sum of digits of {num} is {sum_digit}.")