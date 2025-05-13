# Nested dictionary for books

num = int(input("Enter the number of books whose details you would like to add: "))

book_dict = {}

for i in range(num):
    unique_book_id = input("Enter the unique book id: ")
    value_dict = {}
    details = int(input("Enter the number of details you want to add: "))
    for j in range(details):
        key = input(f"Enter the name of {j+1} detail: ")
        value = input(f"Enter the name of {j+1} details value: ")
        value_dict[key] = value
    book_dict[unique_book_id] = value_dict
print(f"The nested dictionary of books is:\n{book_dict}")


