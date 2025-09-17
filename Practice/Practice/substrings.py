# Generate all substring of string

def find_Substring(s):
    substrings = []
    for i in range(len(s)):
        for j in range(i,len(s)):
            substrings.append(s[i:j+1])
    return substrings

your_Str = input("Enter the string: ")

print(f"Original String: {your_Str}")
print(f"The substrings are the follows: {find_Substring(your_Str)}")