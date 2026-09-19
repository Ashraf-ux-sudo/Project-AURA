tasks = [
    {
        "subject": "Physics",
        "priority": "High",
        "mastery": 72,
        "completed": False
    },
    {
        "subject": "Chemistry",
        "priority": "High",
        "mastery": 48,
        "completed": False
    },
    {
        "subject": "Mathematics",
        "priority": "Medium",
        "mastery": 81,
        "completed": True
    },
    {
        "subject": "Python",
        "priority": "Low",
        "mastery": 90,
        "completed": False
    },
    {
        "subject": "Chemistry",
        "priority": "Medium",
        "mastery": 55,
        "completed": False
    }
]
print("Total number of tasks:", len(tasks))
tasks_completed = 0
tasks_pending = 0 
for task in tasks:
    if task["completed"]:
        tasks_completed += 1
    else:
        tasks_pending += 1
print(f"Completed tasks: {tasks_completed}")
print(f"Pending tasks: {tasks_pending}")

high_priority_pending_tasks = 0
for task in tasks:
    if task["priority"] == "High" and not task["completed"]:
        high_priority_pending_tasks += 1
print(f"High-priority pending tasks : {high_priority_pending_tasks}")

print("Lowest mastery among pending tasks:")
lowest_mastery = 100
lowest_mastery_subject = ""
for task in tasks:
    if not task["completed"] and task["mastery"] < lowest_mastery:
        lowest_mastery_subject = task["subject"]
        lowest_mastery = task["mastery"]
print(f"{lowest_mastery_subject}\nMastery: {lowest_mastery}")

print("subjects below 60:")
for task in tasks:
    if task["mastery"] < 60:
        print("-", task["subject"])

print("Tasks needing immediate attention:")
for task in tasks:
    if not task["completed"] and task["priority"] == "High" and task["mastery"] < 60:
        print("-", task["subject"])