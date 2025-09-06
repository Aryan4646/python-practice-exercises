# Count digits in number



num = int(input("Enter the number: "))

# using string
# print(f"{num} has {len(str(num))} digits.")

# Using loops
def count_digits(n):
    if n == 0:
        return 1  
    n = abs(n)
    count = 0
    while n > 0:
        count +=1
        n //= 10
    return count

print(f"{num} has {count_digits(num)} digits.")