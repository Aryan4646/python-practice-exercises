# Check if string is palindrome

def pali(s):
    output = ""
    for i in range(len(s)-1,-1,-1):
        if s[i] == " ":
            pass
        else:
            output += s[i]
    return output
def remove_whitespace(s):
    output = ""
    for i in s:
        if i == " ":
            pass
        else:
            output += i
    return output.lower()
input_string = input("Enter the string: ")

print(f"Input string: {input_string}")

is_palindrome = pali(input_string)
x = remove_whitespace(input_string)

if is_palindrome.lower() == x:
    print(f"String is palindrome.")
else:
    print(f"String is not palindrome")

