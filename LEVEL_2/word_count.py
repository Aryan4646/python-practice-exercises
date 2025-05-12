# Word count in a sentence (function)
def count_word(strr):
    count = 0
    z = 1
    for i in strr:
        if i != " " and z :
            count += 1
            z = 0
        elif i == " ":
            z = 1
    return count

strr = input("Enter the string: ")

print(f"The string is: {strr}\nand number of words in the string :{count_word(strr)}")
