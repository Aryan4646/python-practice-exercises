num = int(input("Enter upto which number you want multiplication table: "))
num2 = int(input("Enter upto where you need multiplication of a number: "))

for i in range(1, num2+1):
    for j in range(1, num+1):
        print(f"{i*j:3}", end="  ")
    print("")
