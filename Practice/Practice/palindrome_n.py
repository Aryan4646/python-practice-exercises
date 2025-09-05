# Check if a number is palindrome

def rev(n):
    num = 0
    while n > 0:
        x = n%10
        num = num*10 + x
        n //=10
    return num

num = int(input("Enter the number which you want to check whether is palindrome or not: "))

if num >= 0:
    pali = rev(num)
    if num == pali:
        print(f"{num} is palindrome")
    else:
        print(f"{num} and {pali} are different so they are not palindrome.")
else:
    print("A negative number can never be palindrome for example -121 palindrome will be 121-.")
