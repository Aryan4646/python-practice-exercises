# Invert a dictionary
dict_1 = {}
new_dict ={}
num1 = int(input("Enter the number of keys-value pairs you want to add in dict 1: "))
for i1 in range(num1):
    key_1 = input(f"Enter the key {i1+1} of dict 1: ")
    value_1 = input(f"Enter the value {i1+1} of dict 1: ")
    dict_1[key_1] = value_1
for key, value in dict_1.items():
    new_dict[value] = key
print(new_dict)