# A program to print the first N prime numbers.

def prime(num):
    for i in range(2,num+1):
        countt = 0
        for j in range(1,i+1):
            if i % j == 0:
                countt += 1
        if countt == 2:
            print(f"{i} is prime.")

num = int(input("Enter the number upto which you want to check prime number: "))

prime(num)



