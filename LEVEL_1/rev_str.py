# Reverse a string (without slicing)
strr = input("Enter the string: ")
new_str = ""
print(f"\nOriginal string is: {strr}")
for i in range((len(strr)-1), -1, -1):
    new_str += strr[i]
print(f"\nReversed string is: {new_str}")