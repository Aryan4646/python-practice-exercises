num = int(input("Enter the number upto which you want fizzbuzz program to run: "))

for i in range(1,num+1):
    if i % 3 == 0 and i % 5 == 0:
        print(f"Fizzbuzz : {i}")
    elif i % 5 == 0:
        print(f"Buzz: {i}")
    elif i % 3 == 0:
        print(f"Fizz: {i}")