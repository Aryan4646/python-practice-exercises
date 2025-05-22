# Given two lists, return a list that contains only the elements common to both lists (intersection).

list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8, 9]

print(f"Input list 1: {list1}")
print(f"Input list 2: {list2}")

# Using list comprehension
intersection_list = [x for x in list1 if x in list2]
print(f"Intersection list: {intersection_list}")

# Using sets
intersection_list = list(set(list1).intersection(set(list2)))
print(f"Intersection list: {intersection_list}")