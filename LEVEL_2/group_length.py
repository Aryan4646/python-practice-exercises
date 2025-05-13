# Group words by length

strr = input("Enter the string: ")
frequency_dict = {}
current_str = ""
count = 0
for i in strr:
    if i == " ":
        if count in frequency_dict:
            frequency_dict[count].append(current_str)
            current_str = ""
            count = 0
        else:
            frequency_dict[count] = [current_str]
            count = 0
            current_str = ""
    else:
        current_str += i
        count += 1
if count in frequency_dict:
    frequency_dict[count].append(current_str)
else:
    frequency_dict[count] = [current_str]
print(f"\nString is:\n{strr}")
print(f"Grouped words by length:\n{frequency_dict}")





