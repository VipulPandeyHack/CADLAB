students = (
    (1, "Amit", (85, 90, 88)),
    (2, "Sara", (78, 82, 80)),
    (3, "Rahul", (92, 91, 95)),
    (4, "Neha", (70, 75, 72))
)

courses = (
    ("CS101", "Python", 3),
    ("CS102", "Data Structures", 4),
    ("CS103", "Algorithms", 4)
)

college = (
    "ABC College",
    "India",
    students,
    courses
)

student_averages = []

for student in college[2]:
    total = sum(student[2])
    avg = total / len(student[2])
    student_averages.append((student[1], avg))

topper = max(student_averages, key=lambda x: x[1])

course_names = tuple(course[1] for course in college[3])

all_data = (
    college[0],
    college[1],
    student_averages,
    topper,
    course_names
)

print(all_data)