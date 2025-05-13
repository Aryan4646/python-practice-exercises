strr = input("Enter the string: ")

frequency_dict = {}

for i in strr:
    if i in frequency_dict:
        frequency_dict[i] = (frequency_dict.get(i))+1
    else:
        frequency_dict[i] = 1
print(f"The string is:\n{strr}")
print(f"Frequency of each character is as follows:\n{frequency_dict}")