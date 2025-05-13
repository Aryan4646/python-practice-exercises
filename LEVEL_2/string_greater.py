# Filter strings longer than 5 characters
string_list = []
num = int(input("Enter number of list you want to add: "))

for i in range(num):
    r = input(f"Enter {i+1} string: ")
    string_list.append(r)
output_list = []

for x in string_list:
    if len(x) > 5 and x not in output_list:
        output_list.append(x)
print(f"String input List:\n{string_list}")
print(f"Strings whose length is greater than 5:\n{output_list}")