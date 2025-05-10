# Count numbers divisible by 3 and 5 (1 to 100)
# count = 0
# for i in range (3,101):
#     if (i % 3 == 0) and (i % 5 == 0):
#         count += 1
#         print(i)
# print(count)


num1 = int(input("Enter the first number whose divisible you want: "))
num2 = int(input("Enter the second number whose divisible you want: "))
up_num = int(input("Upto which number you want the number: "))
count = 0
for i in range((num1*num2), up_num+1):
    if (i % num1 == 0) and (i % num2 == 0):
        count += 1
        print(f"The {count} divisible of {num1} & {num2} is {i}.")
print(f"The count of divisble number is : {count}")
