# Armstrong number check

def armstrong_check(n):
    new_num = 0
    length_num = len(str(n))
    while n > 0:
        x = n % 10
        new_num += x ** length_num
        n //= 10
    return new_num

num = int(input("Enter the number you want to check: "))
is_armstrong = armstrong_check(num)

if is_armstrong == num:
    print(f"Yes {num} is armstrong.")
else:
    print(f"No {num} is not armstrong")