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
        current_str += i

if current_str in frequency_dict:
    frequency_dict[current_str] = frequency_dict.get(current_str) + 1
else:
    frequency_dict[current_str] = 1
print(f"\nThe string is:\n{strr}")
print(f"Frequency of each word is as follows:\n{frequency_dict}")
