# Find longest word in a sentence

strr = input("Enter the string: ")
print(f"\nThe original string is: {strr}")

maxx = ""
new_max = ""

for i in strr:
    if i != " ":
        new_max += i
    else:
        if len(maxx) < len(new_max):
            maxx = ""
            maxx += new_max
            new_max = ""
        else:
            new_max = ""
if len(maxx) < len(new_max):
    maxx = new_max
print(f"\nThe longest word in the sentence: {maxx}")



