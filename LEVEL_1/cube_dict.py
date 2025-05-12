# Dictionary of cubes (1–10)
num = int(input("Enter the number till which you want dictionary of cubes: "))
cube_dict = {x: x**3 for x in range(1, num+1)}

print(f"The dictionary from 1 to {num} is as follows:\n{cube_dict}")