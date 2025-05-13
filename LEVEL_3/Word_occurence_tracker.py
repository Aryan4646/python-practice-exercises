# Word Occurrence Tracker (ignore punctuation/case)

strr = input("Enter your string: ")
word_dict = {}
new_str = ""
for i in strr:
    if i == " ":
        if new_str in word_dict:
            word_dict[new_str] = word_dict.get(new_str) + 1
            new_str = ""
        else:
            word_dict[new_str] = 1
            new_str = ""
    elif i.isalpha():
        new_str += i.casefold()
if new_str in word_dict:
    word_dict[new_str] = word_dict.get(new_str) + 1
else:
     word_dict[new_str] = 1
print(f"Word occurence tracked as follows:\n{word_dict}")
