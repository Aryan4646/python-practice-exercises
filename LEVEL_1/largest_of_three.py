num1 = float(input("Enter the number 1: "))
num2 = float(input("Enter the number 2: "))
num3 = float(input("Enter the number 3: "))

print(f"\nThe number 1 is: {num1}")
print(f"The number 2 is: {num2}")
print(f"The number 3 is: {num3}\n")

if num1 == num2 == num3:
    print("All numbers are equal.")

elif num1 == num2:
    if num1 > num3:
        print(f"{num1} & {num2} are largest.")
        print(f"{num3} is smallest.")
    else:
        print(f"{num3} is largest.")
        print(f"{num1} & {num2} are smallest.")

elif num1 == num3:
    if num1 > num2:
        print(f"{num1} & {num3} are largest.")
        print(f"{num2} is smallest.")
    else:
        print(f"{num2} is largest.")
        print(f"{num1} & {num3} are smallest.")

elif num2 == num3:
    if num2 > num1:
        print(f"{num2} & {num3} are largest.")
        print(f"{num1} is smallest.")
    else:
        print(f"{num1} is largest.")
        print(f"{num2} & {num3} are smallest.")

else:
    if num1 > num2 and num1 > num3:
        print(f"{num1} is largest.")
        if num2 > num3:
            print(f"{num2} is second largest.")
            print(f"{num3} is smallest.")
        else:
            print(f"{num3} is second largest.")
            print(f"{num2} is smallest.")

    elif num2 > num1 and num2 > num3:
        print(f"{num2} is largest.")
        if num1 > num3:
            print(f"{num1} is second largest.")
            print(f"{num3} is smallest.")
        else:
            print(f"{num3} is second largest.")
            print(f"{num1} is smallest.")

    else:
        print(f"{num3} is largest.")
        if num1 > num2:
            print(f"{num1} is second largest.")
            print(f"{num2} is smallest.")
        else:
            print(f"{num2} is second largest.")
            print(f"{num1} is smallest.")

