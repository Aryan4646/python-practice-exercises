# Sum of first N natural numbers

num = int(input("Enter the number upto which sum you want: "))

if num > 0:
#     res = 0
#     for i in range(1,num+1):
#         res += i
#     print(f"Sum of first {num} natural numbers: {res}")

#     You can also use mathematical formula
    res = (num*(num+1))/2
    print(f"Sum of first {num} natural numbers: {res}")


elif num ==0:
    print(f"Natural numbers start from 1. You entered {num}.")
else:
    print(f"Natural number are positive you wrote a negative number i.e.{num}")

