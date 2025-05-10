# Program to find area and perimeter of a rectangle

length = float(input("Enter the length of rectangle: "))  # Taking input of length from user
breadth = float(input("Enter the breadth of rectangle: "))  # Taking input of breadth from user

area_of_rec = (length*breadth)  # Calculated area using formula i.e. area = length * breadth
peri_of_rec = (2*(length+breadth))  # Calculated perimeter using formula i.e. perimeter = 2(length+breadth)

print(f"\nLength and breadth of rectangle are: {length} & {breadth} respectively\n")
print(f"The calculated area of rectangle is: {area_of_rec}")
print(f"The calculated perimeter of rectangle is: {peri_of_rec} ")





