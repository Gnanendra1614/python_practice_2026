import json

student = {
    "name": "Gnanendra",
    "age": 22,
    "skills": ["Python", "SQL"]
}

with open("student.json", "w") as file:
    json.dump(student, file, indent=4)