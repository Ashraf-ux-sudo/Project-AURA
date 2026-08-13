while True:
 print("1.Add students")
 print("2.View students")
 print("3.Search student")
 print("4.Clear records")
 print("5.Exit")

 choice= input("Enter your choice:")
 if choice=="1":
    name= input("Enter students name:")

    marks = input("Enter marks: ")

    with open("marks.txt1","a") as file:
          file.write(f"{name} - {marks}\n")
    print("Student Added.")        
  
 elif choice=="2":
  print("\nstudent Records:\n")

  with open("marks.txt1","r") as file:
     data = file.read()
     print(data)
 elif choice=="3":
    name = input("Enter student to be searched:")
    found = False
    with open("marks.txt1","r") as file:
     for line in file:
       if name in line:
         found = True
         print(line)
         break
     if not found:
        print("Student not found.")
 elif choice=="4":
     with open("marks.txt1","w") as file:
       file.write("")
     print("All names Cleared")

 elif choice=="5":
    print("Thank you! Goodbye.")
    break

 else:
    print("Invalid choice.")



    
