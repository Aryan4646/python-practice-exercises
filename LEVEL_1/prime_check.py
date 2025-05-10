num = int(input("Enter the number: "))
count = 0
if num <= 1:
    print(f"The number {num} is not prime.")
else:
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    if count == 2:
        print(f"The number {num} is prime.")
    else:
        print(f"The number {num} is not prime.")

