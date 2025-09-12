# Convert string to uppercase

def convert_String(s):
    new_str = ""
    for i in s:
        if ord(i) >= 97 and ord(i) <= 122:
            new_str += chr(ord(i)-32)
        else:
            new_str += i
    return new_str

input_string = input("Enter the string: ")
print(f"Input String: {input_string}")
print(f"Converted string to upper: {convert_String(input_string)}")