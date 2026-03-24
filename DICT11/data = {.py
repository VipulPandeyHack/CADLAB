data = {
    "users": [
        {
            "id": 1,
            "name": "Amit",
            "age": 25,
            "email": "amit@example.com",
            "skills": ["Python", "Django", "SQL"],
            "address": {
                "city": "Kanpur",
                "state": "UP",
                "pincode": 208001
            }
        },
        {
            "id": 2,
            "name": "Sara",
            "age": 28,
            "email": "sara@example.com",
            "skills": ["JavaScript", "React", "Node"],
            "address": {
                "city": "Delhi",
                "state": "Delhi",
                "pincode": 110001
            }
        }
    ],
    "company": {
        "name": "TechSoft",
        "location": "India",
        "departments": {
            "development": {
                "employees": 50,
                "technologies": ["Python", "Java", "C++"]
            },
            "marketing": {
                "employees": 20,
                "channels": ["SEO", "Social Media", "Email"]
            },
            "hr": {
                "employees": 10,
                "policies": ["Leave", "Payroll", "Recruitment"]
            }
        }
    },
    "projects": [
        {
            "project_id": 101,
            "title": "E-commerce Website",
            "status": "In Progress",
            "team": ["Amit", "Sara"]
        },
        {
            "project_id": 102,
            "title": "Mobile App",
            "status": "Completed",
            "team": ["Sara"]
        }
    ]
}

print(data["users"][0]["name"])
print(data["company"]["departments"]["development"]["technologies"])
print(data["projects"][1]["title"])