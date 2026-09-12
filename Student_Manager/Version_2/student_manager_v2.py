class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        self.subjects = []
        self.tasks = []
        self.schedule = []
        self.test_records = []

    def add_subject(self, subject):
        self.subjects.append(subject)

    def view_subjects(self):
        if self.subjects:
            print("Subjects:")
            for subject in self.subjects:
                print("\nSubject:", subject.name)
                print("Completed Topics:")
                for topic in subject.topics_completed:
                    print("-", topic)
                print("Current Topic:", subject.current_topic)
                print("Next Topic:", subject.next_topic)
                print("Mastery:")
                for topic, score in subject.mastery.items():
                    print("-", topic, ":", score, "/ 10")
        else:
            print("No subjects added.")

    def add_task(self, task):
        self.tasks.append(task)

    def view_tasks(self):
        if self.tasks:
            print("Tasks:")
            for task in self.tasks:
                print("Subject:", task.subject.name)
                print("Current topic:", task.subject.current_topic)
                print("Next topic:", task.subject.next_topic)
                print("Topic:", task.topic)
                print("Description:", task.description)
                print("Deadline:", task.deadline)
                print("Priority:", task.priority)
                print("Status:", task.get_status())
                print()
        else:
            print("No tasks added.")

    def add_schedule(self, schedule_item):
        self.schedule.append(schedule_item)

    def view_schedule(self):
        if self.schedule:
            print("Schedule:")
            for item in self.schedule:
                item.view()
                print()
        else:
            print("No schedule items added.")

    def add_test(self, test):
        self.test_records.append(test)

    def view_tests(self):
        if self.test_records:
            print("Test Records:")
            for test in self.test_records:
                print("Subject:", test.subject.name)
                print("Test:", test.test_name)
                print("Marks:", test.marks_obtained, "/", test.max_marks)
                print("Percentage:", test.calculate_percentage(), "%")
                print("Current Topic:", test.subject.current_topic)
                print("Next Topic:", test.subject.next_topic)
                print()
        else:
            print("No test records added.")

    def get_subject(self, name):
        for subject in self.subjects:
            if subject.name.lower() == name.lower():
                return subject
        return None

    def get_pending_tasks(self):
        pending_tasks = []
        for task in self.tasks:
            if not task.is_completed():
                pending_tasks.append(task)
        return pending_tasks

    def get_completed_tasks(self):
        completed_tasks = []
        for task in self.tasks:
            if task.is_completed():
                completed_tasks.append(task)
        return completed_tasks

    def get_test_average(self):
        if not self.test_records:
            return 0

        total = 0
        for test in self.test_records:
            total += test.calculate_percentage()
        return total / len(self.test_records)

    def get_highest_priority_task(self):
        pending_tasks = self.get_pending_tasks()
        if not pending_tasks:
            return None

        priority_order = {
            "High": 3,
            "Medium": 2,
            "Low": 1
        }

        highest_task = pending_tasks[0]
        for task in pending_tasks:
            if priority_order.get(task.priority, 0) > priority_order.get(
                highest_task.priority, 0
            ):
                highest_task = task

        return highest_task

    def get_pending_task_count(self):
        return len(self.get_pending_tasks())

    def get_completed_task_count(self):
        return len(self.get_completed_tasks())

    def get_tasks_by_priority(self, priority):
        matching_tasks = []
        for task in self.tasks:
            if not task.is_completed() and task.priority.lower() == priority.lower():
                matching_tasks.append(task)
        return matching_tasks

    def view_task_summary(self):
        completed_tasks = self.get_completed_tasks()
        pending_tasks = self.get_pending_tasks()

        print("Task Summary:")
        print("Completed tasks:", len(completed_tasks))
        for task in completed_tasks:
            print("-", task.topic)

        print("Pending tasks:", len(pending_tasks))
        for task in pending_tasks:
            print("-", task.topic)

    def get_schedule_for_day(self, day):
        matching_items = []
        for item in self.schedule:
            if item.day.lower() == day.lower():
                matching_items.append(item)
        return matching_items

    def get_next_schedule(self):
        if not self.schedule:
            return None
        return self.schedule[0]

    def get_schedule_for_subject(self, subject_name):
        matching_items = []
        for item in self.schedule:
            if item.subject and item.subject.name.lower() == subject_name.lower():
                matching_items.append(item)
        return matching_items

    def get_schedule_for_topic(self, topic):
        matching_items = []
        for item in self.schedule:
            if item.topic and item.topic.lower() == topic.lower():
                matching_items.append(item)
        return matching_items

    def has_schedule(self):
        return bool(self.schedule)

    def has_tests(self):
        return bool(self.test_records)

    def get_subject_count(self):
        return len(self.subjects)

    def get_weakest_subject(self):
        if not self.subjects:
            return None

        weakest_subject = None
        lowest_average = float("inf")

        for subject in self.subjects:
            average = subject.get_average_mastery()
            if average is not None and average < lowest_average:
                lowest_average = average
                weakest_subject = subject

        return weakest_subject

    def get_weakest_subject_average(self):
        weakest_subject = self.get_weakest_subject()
        if weakest_subject is None:
            return None
        return weakest_subject.get_average_mastery()

    def get_academic_summary(self):
        weakest_subject = self.get_weakest_subject()
        if weakest_subject is None:
            return None

        return {
            "subject_count": self.get_subject_count(),
            "weakest_subject": weakest_subject.name,
            "weakest_subject_average": weakest_subject.get_average_mastery()
        }

    def get_student_summary(self):
        academic = self.get_academic_summary()

        return {
            "name": self.name,
            "grade": self.grade,
            "subjects": self.get_subject_count(),
            "pending_tasks": self.get_pending_task_count(),
            "completed_tasks": self.get_completed_task_count(),
            "average_test_percentage": self.get_test_average(),
            "weakest_subject": academic["weakest_subject"] if academic else None,
            "weakest_subject_average": (
                academic["weakest_subject_average"] if academic else None
            )
        }

    def get_urgent_tasks(self):
        urgent_tasks = []
        for task in self.tasks:
            if not task.is_completed() and task.priority.lower() == "high":
                urgent_tasks.append(task)
        return urgent_tasks

    def get_pending_tasks_by_deadline(self, deadline):
        matching_tasks = []
        for task in self.tasks:
            if not task.is_completed() and task.deadline.lower() == deadline.lower():
                matching_tasks.append(task)
        return matching_tasks

    def get_pending_tasks_by_deadline_and_priority(self, deadline, priority):
        matching_tasks = []
        for task in self.tasks:
            if (
                not task.is_completed()
                and task.deadline.lower() == deadline.lower()
                and task.priority.lower() == priority.lower()
            ):
                matching_tasks.append(task)
        return matching_tasks


class Subject:
    def __init__(self, name):
        self.name = name
        self.topics_completed = []
        self.current_topic = None
        self.next_topic = None
        self.mastery = {}

    def add_completed_topic(self, topic):
        self.topics_completed.append(topic)

    def set_topics(self, current_topic, next_topic):
        self.current_topic = current_topic
        self.next_topic = next_topic

    def set_mastery(self, topic, score):
        self.mastery[topic] = score

    def get_mastery(self, topic):
        return self.mastery.get(topic)

    def get_lowest_mastery_topic(self):
        if not self.mastery:
            return None

        lowest_topic = None
        lowest_score = float("inf")

        for topic, score in self.mastery.items():
            if score < lowest_score:
                lowest_score = score
                lowest_topic = topic

        return lowest_topic

    def get_lowest_mastery_score(self):
        if not self.mastery:
            return None

        return min(self.mastery.values())

    def get_average_mastery(self):
        if not self.mastery:
            return None

        return sum(self.mastery.values()) / len(self.mastery)

    def get_mastery_summary(self):
        if not self.mastery:
            return None

        return {
            "average": self.get_average_mastery(),
            "lowest_topic": self.get_lowest_mastery_topic(),
            "lowest_score": self.get_lowest_mastery_score()
        }


class Task:
    def __init__(self, subject, topic, description, deadline, priority):
        self.subject = subject
        self.topic = topic
        self.description = description
        self.deadline = deadline
        self.priority = priority
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def is_completed(self):
        return self.completed

    def get_status(self):
        if self.completed:
            return f"Completed: {self.topic}"
        return f"Pending: {self.topic}"


class ScheduleItem:
    def __init__(self, day, start_time, end_time, activity, subject=None, topic=None):
        self.day = day
        self.start_time = start_time
        self.end_time = end_time
        self.activity = activity
        self.subject = subject
        self.topic = topic

    def view(self):
        print("Day:", self.day)
        print("Time:", self.start_time, "-", self.end_time)
        print("Activity:", self.activity)

        if self.subject:
            print("Subject:", self.subject.name)

        if self.topic:
            print("Topic:", self.topic)

    def update_topic(self, topic):
        self.topic = topic


class TestRecord:
    def __init__(self, subject, test_name, marks_obtained, max_marks):
        self.subject = subject
        self.test_name = test_name
        self.marks_obtained = marks_obtained
        self.max_marks = max_marks

    def calculate_percentage(self):
        return (self.marks_obtained / self.max_marks) * 100

    def update_marks(self, marks_obtained):
        self.marks_obtained = marks_obtained


if __name__ == "__main__":
    name = input("Enter Student name: ")
    grade = int(input("Enter Student Grade: "))

    student = Student(name, grade)

    physics = Subject("Physics")
    physics.add_completed_topic("Ray Optics")
    physics.add_completed_topic("Wave Optics")
    physics.set_topics("Nuclei", "Radioactivity")
    physics.set_mastery("Ray Optics", 9)
    physics.set_mastery("Wave Optics", 8)
    physics.set_mastery("Nuclei", 6)
    student.add_subject(physics)

    physics_task = Task(
        physics,
        "Nuclei",
        "Complete Nuclei questions",
        "Saturday",
        "High"
    )
    physics_task.mark_completed()
    student.add_task(physics_task)

    unfinished_task = Task(
        physics,
        "Radioactivity",
        "Study Radioactivity",
        "Sunday",
        "High"
    )
    student.add_task(unfinished_task)

    physics_session = ScheduleItem(
        "Monday",
        "5:00 PM",
        "6:30 PM",
        "Study",
        physics,
        "Nuclei"
    )
    student.add_schedule(physics_session)

    physics_test = TestRecord(physics, "Weekly Test", 60, 100)
    student.add_test(physics_test)

    student.view_subjects()
    student.view_tasks()
    student.view_schedule()
    student.view_tests()
    student.view_task_summary()

    summary = student.get_student_summary()
    print("Student Summary:")
    print("Name:", summary["name"])
    print("Grade:", summary["grade"])
    print("Subjects:", summary["subjects"])
    print("Pending tasks:", summary["pending_tasks"])
    print("Completed tasks:", summary["completed_tasks"])
    print("Average test percentage:", round(summary["average_test_percentage"], 2), "%")
    print("Weakest subject:", summary["weakest_subject"])
    print(
        "Weakest subject average:",
        round(summary["weakest_subject_average"], 2),
        "/ 10"
    )

    urgent_tasks = student.get_urgent_tasks()
    print("Urgent tasks:", len(urgent_tasks))
    for task in urgent_tasks:
        print("-", task.topic)
