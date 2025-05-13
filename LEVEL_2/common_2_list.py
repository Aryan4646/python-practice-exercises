# Common elements between two lists (no sets)

input_list_1 = [1, 5, 3, 6, 4]
input_list_2 = [2, 5, 3, 4, 6]

common_list = []

if len(input_list_1) >= len(input_list_2):
    for i in input_list_1:
        if i in input_list_2 and i not in common_list:
            common_list.append(i)
else:
    for i in input_list_2:
        if i in input_list_1 and i not in common_list:
            common_list.append(i)
print(f"List1: {input_list_1}")
print(f"List2: {input_list_2}")
print(f"Common List:{common_list}")