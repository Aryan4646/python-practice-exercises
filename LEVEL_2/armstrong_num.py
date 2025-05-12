num = int(input("Enter the number you want to check is armstrong or not: "))
sum = 0
fake_num = num
length = len(str(num))
if num > 0:
    while fake_num > 0:
        r = fake_num % 10
        sum += r**length
        fake_num //= 10
    if sum == num:
        print(f"{num} is a armstrong number.")
    else:
        print(f"{num} is not a armstrong number")
else:
    print("Enter a valid positive number")

