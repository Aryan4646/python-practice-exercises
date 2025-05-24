# Implement nested try-except blocks to handle multiple types of errors in a single function.

def multiple_err(t):
    try:
        with open(t, "r") as file:
            for i in file:
                try:
                    p = int(i)
                    print(p)
                except ValueError:
                    print(f"String can not be converted to integer value. String was: {i.strip()}")
    except FileNotFoundError:
        print("File does not exist")
    try:
        num1 = int(input("Enter the number 1: "))
        num2 = int(input("Enter the number 2: "))
        try:
            print(f"Num1 divided by Num2 is: {num1/num2}")
        except ZeroDivisionError:
            print("Zero divison error")
    except ValueError:
        print("Only integer can be divided")

multiple_err("txtt")