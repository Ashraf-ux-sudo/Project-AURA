subjects = [
    {"name": "Physics", "mastery": 72},
    {"name": "Chemistry", "mastery": 48},
    {"name": "Mathematics", "mastery": 81},
    {"name": "Python", "mastery": 90}
]
average_mastery = 0
highest_mastery = 0
strongest_subject = ""
lowest_mastery = 100
weakest_subject = ""
for subject in subjects:
    average_mastery += subject["mastery"]
    if subject["mastery"] > highest_mastery:
        highest_mastery = subject["mastery"]
        strongest_subject = subject["name"]
    if subject["mastery"] < lowest_mastery:
        lowest_mastery = subject["mastery"]
        weakest_subject =subject["name"]


average_mastery /= len(subjects)
print("Average mastery :", average_mastery, "%")
print("Highest mastery :", highest_mastery, "%")
print("Strongest subject :", strongest_subject)
print("Lowest mastery : ", lowest_mastery, "%")
print("Weakest subject :", weakest_subject)

print("Subjects needing attention:")
for subject in subjects:
    if subject["mastery"] < 60:
        print("-", subject["name"])
