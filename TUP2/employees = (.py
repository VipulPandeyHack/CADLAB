employees = (
    (101, "Amit", "Developer", (50000, 2000, 1500)),
    (102, "Sara", "Designer", (45000, 1500, 1200)),
    (103, "Rahul", "Manager", (70000, 3000, 2500)),
    (104, "Neha", "Tester", (40000, 1200, 1000))
)

departments = (
    ("IT", (101, 102, 104)),
    ("Management", (103,))
)

company = (
    "TechCorp",
    "India",
    employees,
    departments
)

salary_summary = []

for emp in company[2]:
    base = emp[3][0]
    bonus = emp[3][1]
    allowance = emp[3][2]
    total_salary = base + bonus + allowance
    salary_summary.append((emp[1], total_salary))

highest_paid = max(salary_summary, key=lambda x: x[1])

dept_employee_count = []

for dept in company[3]:
    count = len(dept[1])
    dept_employee_count.append((dept[0], count))

final_data = (
    company[0],
    salary_summary,
    highest_paid,
    tuple(dept_employee_count)
)

print(final_data)