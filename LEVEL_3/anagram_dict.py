def mydict(strr):
    d = {}
    for i in strr:
        i = i.casefold()
        if i.isalpha():
            if i in d:
                d[i] = d.get(i)+1
            else:
                d[i] = 1
    return d

str1 = input(f"Enter the string 1: ")
str2 = input(f"Enter the string 1: ")

dict1 = mydict(str1)
dict2 = mydict(str2)

if dict1 == dict2:
    print("Anagram")
else:
    print("Not Anagram")