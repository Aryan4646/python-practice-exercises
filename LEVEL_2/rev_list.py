# Reverse a list using your own function
def output_l(input_list):
    output_li = []
    n = (len(input_list)-1)
    for i in range(n, -1, -1):
        output_li.append(input_list[i])
    return output_li

num = int(input("Enter the number of elements you want to add in list: "))
input_list = []

for i in range(num):
    a = float(input(f"Enter the {i+1} element of list: "))
    input_list.append(a)
print(f"The original list is:\n{input_list}")
print(f"The modified list is:\n{output_l(input_list)}")