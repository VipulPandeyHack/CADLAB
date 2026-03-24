library = {
    "books": [
        {
            "isbn": "111",
            "title": "Python Basics",
            "author": "John Doe",
            "available": True,
            "ratings": [4, 5, 3, 4],
            "publisher": {
                "name": "TechBooks",
                "year": 2020
            }
        },
        {
            "isbn": "222",
            "title": "Advanced Python",
            "author": "Jane Smith",
            "available": False,
            "ratings": [5, 5, 4, 5],
            "publisher": {
                "name": "CodePress",
                "year": 2022
            }
        }
    ],
    "members": [
        {
            "id": 1,
            "name": "Rahul",
            "borrowed": ["111"],
            "fine": 0
        },
        {
            "id": 2,
            "name": "Neha",
            "borrowed": [],
            "fine": 50
        }
    ],
    "staff": {
        "librarian": {
            "name": "Mr. Sharma",
            "experience": 10
        },
        "assistants": [
            {"name": "Ravi", "shift": "morning"},
            {"name": "Anita", "shift": "evening"}
        ]
    }
}

library["members"][0]["borrowed"].append("222")
library["books"][1]["available"] = True
total_ratings = sum(library["books"][0]["ratings"])
average_rating = total_ratings / len(library["books"][0]["ratings"])
library["books"][0]["average_rating"] = average_rating
print(library)