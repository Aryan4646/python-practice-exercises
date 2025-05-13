# Unique word count in a sentence
strr = input("Enter the string: ")
frequency_dict = {}
current_str = ""
for i in strr:
    if i == " ":
        if current_str in frequency_dict:
            frequency_dict[current_str] = frequency_dict.get(current_str) + 1
        else:
            frequency_dict[current_str] = 1
        current_str =""
    elif i.isalpha():
        current_str += i.casefold()

if current_str in frequency_dict:
    frequency_dict[current_str] = frequency_dict.get(current_str) + 1
else:
    frequency_dict[current_str] = 1
unique_count = len(frequency_dict)
print(f"\nThe string is:\n{strr}")
print(f"Frequency of each word is as follows:\n{frequency_dict}")
print(f"Unique word count is: {unique_count}")