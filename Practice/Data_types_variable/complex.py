# A function to check if a complex number’s real part is positive.
def positive_check(a):
    if a.real >= 0:
        s = "positive"
    else:
        s = "negative"
    return s

positive = float(input("Enter the real part: "))
negative = float(input("Enter the imaginary part: "))

complex_num = complex(positive,negative)
print(complex_num)

print(f"The complex number real part is: {positive_check(complex_num)}")

