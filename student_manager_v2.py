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
                    print("Completed:", task.completed)
                    print()
            else:
             print("No tasks added.")        

    def add_schedule(self,schedule_item):
            self.schedule.append(schedule_item)

    def view_schedule(self):
            if self.schedule:
                print("Schedule:")
    
                for item in self.schedule:
                    print("Day:", item.day)
                    print("Time:", item.start_time, "-", item.end_time)
                    print("Activity:", item.activity)
    
                    if item.subject:
                        print("Subject:", item.subject.name)
                        print("Current Topic:", item.subject.current_topic)
                        print("Next Topic:", item.subject.next_topic)

                    if item.topic:    
                        print("Topic:", item.topic)
    
                    print()
            else:
                print("No schedule items added.")    


    def add_test(self, test):
        self.test_records.append(test)

    def view_tests(self):
        if self.test_records:
            print("test Records:")

            for test in self.test_records:
                print("Subject:", test.subject.name)
                print("Test:", test.test_name)
                print("Marks:", test.marks_obtained, "/", test.max_marks)
                print("Percentage:", test.percentage, "%")
                print("Current Topic:", test.subject.current_topic)
                print("Next Topic:", test.subject.next_topic)
                print()
        else:
            print("No test records added.")        
            
class Subject:
    def __init__(self,name):
        self.name = name
        self.topics_completed = []
        self.current_topic = None
        self.next_topic = None
        self.mastery = {}

physics = Subject("Physics")

physics.topics_completed = ["Ray Optics","Wave Optics"]
physics.current_topic = "Nuclei"
physics.next_topic = "Radioactivity"
physics.mastery = {"Ray Optics":9,"Wave Optics":8,"Nuclei":6}


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
        print("Task marked as completed.")

physics_task = Task( physics, "Thermodynamics","Complete Thermodynamics questions","Saturday", "High")

physics_task.mark_completed()
print(physics_task.completed)

class ScheduleItem:
    def __init__(self, day, start_time, end_time, activity, subject=None, topic=None):
        self.day = day
        self.start_time = start_time
        self.end_time = end_time
        self.activity = activity
        self.subject = subject
        self.topic = topic

physics_session = ScheduleItem(
    "Monday",
    "5:00 PM",
    "6:30 PM",
    "Study",
    physics,
    "Thermodynamics"
    )


class TestRecord:
    def __init__(self, subject, test_name, marks_obtained, max_marks):
        self.subject = subject
        self.test_name = test_name
        self.marks_obtained = marks_obtained
        self.max_marks = max_marks
        self.percentage = (marks_obtained/max_marks)*100

physics_test = TestRecord(physics, "Weekly Test", 60, 100)




student = Student("Ashraf",12)        
student.add_subject(physics)

student.view_subjects()
student.add_task(physics_task)
student.view_tasks()
student.add_schedule(physics_session)
student.view_schedule()
student.add_test(physics_test)
student.view_tests()

