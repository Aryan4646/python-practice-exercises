# Rotate list position to the right
num = int(input("Enter the number of elements you want to add in list: "))
input_list = []
output_list = []
for i in range(num):
    list_element = float(input(f"Enter the {i+1} element of the list: "))
    input_list.append(list_element)
rotation = int(input("\nEnter how many position you want to push: "))
rotation = rotation % num  # Because if num is 5 and rotation is 7 then 2 is similar
for x in range(rotation):
    output_list.append(input_list[(num-1)-x])
# output list that is generated till now must be reversed
output_list = output_list[::-1]
for x in range(num-rotation):
    output_list.append(input_list[x])
print(f"Input List is :\n{input_list}")
print(f"Output List is: \n{output_list}")

