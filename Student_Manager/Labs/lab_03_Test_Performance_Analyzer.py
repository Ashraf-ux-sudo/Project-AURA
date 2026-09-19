test_records = [
    {"subject": "Physics", "score": 78, "total": 100},
    {"subject": "Chemistry", "score": 52, "total": 100},
    {"subject": "Mathematics", "score": 91, "total": 100},
    {"subject": "Python", "score": 84, "total": 100}
]
average_score = 0
highest_score = 0
highest_scoring_subject = ""
lowest_score = 100
lowest_scoring_subject = ""
for record in test_records:
    average_score += record["score"]
    if record["score"] > highest_score:
        highest_score = record["score"]
        highest_scoring_subject = record["subject"]
    if record["score"] < lowest_score:
        lowest_score = record["score"]
        lowest_scoring_subject = record["subject"]
average_score /= len(test_records)
print("Average score :", average_score)
print("Highest scoring subject :", highest_scoring_subject)
print("Highest score :", highest_score)
print("Lowest scoring subject :", lowest_scoring_subject)
print("Lowest score:", lowest_score)

print("Subjects needing improvement:")
subjects_below_60 = 0
for record in test_records:
    if record["score"] < 60:
        subjects_below_60 += 1
        print("-", record["subject"])
print("Number of subjects needing improvement:", subjects_below_60)