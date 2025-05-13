# Mini Contact Book:
# Add contact
# Search contact
# Delete contact

contact_dict = {"SS": 7023, "aa": 7483, "zz": 7382}  # Took a sample dictionary
print("1.Add Contact: 1\n2.Search Contact: 2\n3.Delete Contact: 3")
operation = int(input("Enter the operation you want to perform: "))

if operation == 1:
    cont_name_Add = input("Enter the name: ")
    cont_number_Add = int(input("Enter the number: "))
    contact_dict[cont_name_Add] = cont_number_Add
    print(f"The New Dict is:\n{contact_dict}")
elif operation == 2:
    cont_name_se = input("Enter the name: ")
    print(f"The number of {cont_name_se} is:{contact_dict.get(cont_name_se,'Missing')} ")
elif operation == 3:
    cont_name_del = input("Enter the name: ")
    if cont_name_del in contact_dict:
        del contact_dict[cont_name_del ]
        print(f"The New Dict is:\n{contact_dict}")
    else:
        print(f"Contact is missing in contact list:\n{contact_dict}")


