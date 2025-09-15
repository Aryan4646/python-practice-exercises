# Replace vowels with ‘*’

def modified(s):
    new_s = ""
    for i in s:
        if i in "aeiouAEIOU":
            new_s += "*"
        else:
            new_s += i
    return new_s

s = "The quick brown fox jumps over the lazy hippopotamus"

print(f"The string is as follows:\n{s}")
print(f"Modified string is as follows:\n{modified(s)}")