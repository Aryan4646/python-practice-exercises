# Fibonacci series up to N terms

# Using recursion
# def fib(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fib(n-1)+fib(n-2)
#
# num = int(input("Enter upto which number you want fibonacci series: "))
#
# print(f"Fibonacci series upto {num} is as follows: ")
# for i in range(num):
#     print(f"{fib(i)}")

# using loops

num = int(input("Enter upto which number you want fibonacci series: "))

print(f"Fibonacci series upto {num} is as follows: ")
fib_list = [0,1]

if num == 0:
    print(fib_list[0])
elif num == 1:
    print(fib_list[0])
    print(fib_list[1])
else:
    for i in range(2,num):
        x = fib_list[i-2]+fib_list[i-1]
        fib_list.append(x)
for i in fib_list:
    print(i)