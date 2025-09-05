# Print first N natural numbers

num = int(input("How many natural numbers you want to print: "))

if num > 0:
    print(f"\n\nFirst {num} natural numbers are: ")
    for i in range(1,num+1):
        print(i,end=" ")
else:
    print(f"\n\n{num} is not a natural number.")
