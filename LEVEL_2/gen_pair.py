# Generate all pairs from two lists
L1 = [1, 2]
L2 = ['a', 'b']

Output_List = []

for i in L1:
    for j in L2:
        r = (i,j)
        Output_List.append(r)
print(Output_List)