# # Remove duplicate characters
strr = input("Enter the string: ")
print(f"\nThe original string is: {strr}")

duplicates = ""
new_str = ""

for i in strr:
    if i not in duplicates:
        new_str += i
        if i != " ":
            duplicates += i
print(f"The Modified string is: {new_str}")





