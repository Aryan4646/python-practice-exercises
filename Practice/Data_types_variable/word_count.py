# Write a function that counts the frequency of each word in a string using a dictionary.

def dict_freq(strr):
    dict = {}
    stringg = ""
    for i in strr.lower():
        if i == " ":
            if stringg not in dict:
                dict[stringg] = 1
                stringg = ""
            else:
                dict[stringg] = dict[stringg]+1
                stringg = ""
        elif i.isalpha():
            stringg += i
    if stringg not in dict:
        dict[stringg] = 1
    else:
        dict[stringg] = dict[stringg]+1
    return dict

input_string = input("Enter the string: ")

print(f"\nThe input string is: {input_string}")
print(f"Frequency of each word in a string is as follows:\n{dict_freq(input_string)}")


