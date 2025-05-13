# Student records
student_rec = []
num = int(input("Enter the number of student records you want to add: "))

for i in range(num):
    d = {}
    d["Name"] = input("Enter the name of student: ")
    d["Marks"] = float(input("Enter the marks: "))
    d["City"] = input("Enter the city name: ")
    student_rec.append(d)
print(f"The student records are as follows:\n{student_rec}")
