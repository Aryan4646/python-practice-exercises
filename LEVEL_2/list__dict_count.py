# List to Dictionary with Count

List_input = ['apple', 'banana', 'apple']
count_dict ={}

for i in List_input:
    if i in count_dict:
        count_dict[i] = count_dict.get(i)+1
    else:
        count_dict[i] = 1
print(f"Dictionary with count:\n{count_dict}")
