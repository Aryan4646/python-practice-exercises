# Find frequency of each character

def frequency_dict(s):
    char_freq = {}
    for i in s:
        if i != " ":
            if i in char_freq:
                char_freq[i] += 1
            else:
                char_freq[i] = 1
    return char_freq
input_Str = input("Enter the string: ")

print(f"Input string: {input_Str}")
print(f"Frequency of each character is as follows: {frequency_dict(input_Str)}")