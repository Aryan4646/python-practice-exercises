def convert_Dict(s):
    dict_created = {}
    for i in s:
        if i.isalnum():
            if i in dict_created:
                dict_created[i] += 1
            else:
                dict_created[i] =1
    return dict_created

def check_anagram(s1,s2):
    s1_dict = convert_Dict(s1)
    s2_dict = convert_Dict(s2)
    if s1_dict == s2_dict:
        return True
    return False

s1 = "listen"
s2 = "silent"

is_true = check_anagram(s1,s2)

if is_true:
    print(f"Yes the strings {s1} and {s2} are anagrams.")
else:
    print(f"No strings are not anagram.")
