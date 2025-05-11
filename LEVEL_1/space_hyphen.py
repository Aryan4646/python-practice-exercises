# Replace spaces with hyphens

strr = input("Enter the string: ")
print(f"\nOriginal string is: {strr}")
new_string = ""
for i in strr:
    if i == " ":
        new_string += "-"
    else:
        new_string += i
print(f"Modified string is: {new_string}")