# Caesar cipher problem
# Not fully functional yet need modification
strr = input("Enter the string: ")
new_str = ""
shift = int(input("Enter the shift you want in position: "))

for i in strr:
    if i.isalpha():
        if i.isupper():
            if (ord(i)+shift) > 90:
                new_str += chr((ord(i)-26) + shift)
            else:
                new_str += chr(ord(i) + shift)
        else:
            if (ord(i)+shift) > 122:
                new_str += chr((ord(i)-26) + shift)
            else:
                new_str += chr(ord(i) + shift)
    else:
        new_str += i
print(f"The orignal string was: {strr}")
print(f"The caesar cipher string is: {new_str}")

