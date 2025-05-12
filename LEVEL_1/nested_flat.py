# Flatten a nested_list
nested = [[1, 2], [3, 4]]
output_list = []

for sublist in nested:
    if type(sublist) == list:
        for item in sublist:
            output_list.append(item)
    else:
        output_list.append(sublist)
print(f"The Original List is: {nested}")
print(f"The Output List is: {output_list}")







        #