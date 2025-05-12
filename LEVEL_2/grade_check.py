# Student grade check {dict of scores >75}
student_scores = {
    "Alice": 88,
    "Bob": 72,
    "Charlie": 95,
    "Diana": 67,
    "Ethan": 78,
    "Fiona": 74
}
seventy_fivePlus = {}
for key, value in student_scores.items():
    if value > 75:
        seventy_fivePlus[key] = value
print(f"Original Dictionary is:\n{student_scores}")
print(f"Greater than 75 students are:\n{seventy_fivePlus}")
