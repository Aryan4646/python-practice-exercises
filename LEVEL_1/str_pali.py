# Check if string is a palindrome
strr = input("Enter the string: ")

# without slicing
# new_str = ""
# print(f"\nOriginal string is: {strr}")
# for i in range((len(strr)-1), -1, -1):
#     new_str += strr[i]

# with slicing
print(f"\nOriginal string is: {strr}\n")
new_str = strr[::-1]

if strr.casefold() == new_str.casefold():
    print(f"String {strr} is palindrome.")
else:
    print(f"String {strr} is not palindrome.")
#     You can create string palindrome
    z = int(input(f"Enter 0 if you want to create the {strr} palindrome\n"))
    if z == 0:
        print(f"The palindrome string is {strr.casefold()+new_str.casefold()}")
    else:
        print(f"You dont want the {strr} to be palindrome.")


