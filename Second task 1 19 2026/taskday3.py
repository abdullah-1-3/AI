"""
Day 4 Activity: Parse nested dictionaries (student database).
Tasks:
1) Get Alice's AI301 grade
2) Calculate Bob's GPA (weighted by credits)
3) Find all students in CS101
4) Get average grade across all courses
5) Find student with highest GPA
"""

students = {
    "S001": {
        "name": "Alice Chen",
        "courses": {
            "CS101": {"grade": 92, "credits": 3},
            "MATH201": {"grade": 88, "credits": 4},
            "AI301": {"grade": 95, "credits": 3},
        },
        "advisor": "Dr. Smith",
    },
    "S002": {
        "name": "Bob Lee",
        "courses": {
            "CS101": {"grade": 85, "credits": 3},
            "MATH201": {"grade": 90, "credits": 4},
        },
        "advisor": "Dr. Patel",
    },
}

# TODO: Implement the tasks above using nested dict access.



alice_ai301 = students["S001"]["courses"]["AI301"]["grade"]

bob_courses = students["S002"]["courses"]
bob_total_points = sum(
    course["grade"] * course["credits"] for course in bob_courses.values()
)
bob_total_credits = sum(course["credits"] for course in bob_courses.values())
bob_gpa = bob_total_points / bob_total_credits

cs101_students = [
    data["name"]
    for data in students.values()
    if "CS101" in data["courses"]
]

all_grades = [
    course["grade"]
    for student in students.values()
    for course in student["courses"].values()
]
average_grade = sum(all_grades) / len(all_grades)

def calculate_gpa(student):
    courses = student["courses"]
    total_points = sum(c["grade"] * c["credits"] for c in courses.values())
    total_credits = sum(c["credits"] for c in courses.values())
    return total_points / total_credits

highest_gpa_student = max(
    students.values(),
    key=lambda s: calculate_gpa(s)
)["name"]

print(alice_ai301)
print(bob_gpa)
print(cs101_students)
print(average_grade)
print(highest_gpa_student)
