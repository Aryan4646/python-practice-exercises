# Reverse a number
def rev(n):
    rev = 0
    if n > 0:
        while n > 0:
            x = n%10
            rev = rev*10 + x
            n //= 10
        return rev
    else:
        n *= -1
        while n > 0:
            x = n%10
            rev = rev*10 + x
            n //= 10
        rev *= -1
    return rev


num = int(input("Enter the number you want to reverse: "))

print(f"\nThe original number: {num} ")
print(f"The reversed number: {rev(num)}")