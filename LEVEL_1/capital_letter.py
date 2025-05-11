# Capitalize first letter of every word
strr = input("Enter the string: ")
print(f"\nThe original string is: {strr}")

# Using title method
# print(f"The Modified string : {strr.title()}")

# # Manually
new_strr = ""
z = 1
for i in range(len(strr)):
    if strr[i] == " ":
        z = 1
        new_strr += strr[i]
    elif z and strr[i].isalpha():
        if 97 <= ord(strr[i]) <= 122:
            ch = chr(ord(strr[i])-32)
            new_strr += ch
        else:
            new_strr += strr[i]
        z = 0
    else:
        new_strr += strr[i]
print(f"\nModified string: {new_strr}")



