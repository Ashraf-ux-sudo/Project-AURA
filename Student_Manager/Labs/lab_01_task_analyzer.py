tasks = [
    {"topic": "Physics", "priority": "High", "completed": False},
    {"topic": "Mathematics", "priority": "Medium", "completed": True},
    {"topic": "Chemistry", "priority": "High", "completed": False},
    {"topic": "Python", "priority": "Low", "completed": True}
]

print("Total tasks completed:", sum(1 for t in tasks if t["completed"]))
print("Total tasks pending:", sum(1 for t in tasks if not t["completed"]))
for task in tasks:
    if task["completed"]:
        print(f"Task '{task['topic']}' is completed.")
    else:
        print(f"Task '{task['topic']}' is pending.")

print("High-priority pendingtasks:", sum(1 for t in tasks if t["priority"] == "High" and not t["completed"]))
for task in tasks:
    if task["priority"] == "High" and not task["completed"]:
        print("High-priority pending task:",  task["topic"])