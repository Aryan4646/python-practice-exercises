def mystr(n):
    strr = input(f"Enter the {n} string: ")
    new_strr = ""
    for i in strr:
        if i == " ":
            pass
        elif ((i.casefold()).isalpha()):
            new_strr += i
    return new_strr

str1 = mystr(1)
str2 = mystr(2)

if len(str1) == len(str2):
    for i in str1:
        if str1.count(i) != str2.count(i):
            print("Not anagram")
            break
    else:
        print("Anagram")
else:
    print("No they are not anagram")




