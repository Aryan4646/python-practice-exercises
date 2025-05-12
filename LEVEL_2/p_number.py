# All prime numbers between 1–num

num = int(input("Enter upto which number you want prime numbers: "))

for i in range(2, num+1):
    count = 0
    for j in range(1, num+1):
        if i % j == 0:
            count += 1
    if count == 2:
        print(f"{i} is a prime number")


