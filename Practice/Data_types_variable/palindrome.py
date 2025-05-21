# Create a program to check if a number is a palindrome (reads same backward).
def check(num,new):
    if num == 0:
        return new
    else:
        new = new * 10 + num % 10
        return check(num//10 , new)


num = int(input("Enter the number: "))
new = 0
palindrome = check(num,new)
if palindrome == num:
    print(f"Yes number {num} is palindrome")
else:
    print(f"No number {num} is palindrome")