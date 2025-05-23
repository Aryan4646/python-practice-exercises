# A function that returns another function to multiply a number by a given factor (closure).
def factor():
    fact = int(input("Enter the factor: "))
    def multiplier():
        number = int(input("Enter the number: "))
        multiplied = number * fact
        return multiplied
    return multiplier
mul = factor()
print(mul())