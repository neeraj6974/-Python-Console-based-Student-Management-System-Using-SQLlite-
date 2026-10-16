import student.stud as s

name = input("Enter the name of the student = ")

print(f"Hello, {name} !")

while(True):
    print("1.Add Student")
    print("2.Display Student")
    print("3.Search Student")
    print("4.Update Student Marks")
    print("5.Delete Student")
    print("6.Exit")

    ch = input("Enter your choice (1/2/3/4/5/6) = ")
    if ch == "1":
        name = input("Enter student name = ")
        age = int(input("Enter age = "))
        course = input("Enter course name = ")
        marks = int(input("Enter student marks = "))

        s.add_student(name , age , course , marks)

    elif ch == "2":
        s.display_student()

    elif ch == "3":
        student_id = int(input("Enter student id = "))
        s.search_student(student_id)

    elif ch == "4":
        student_id = int(input("Enter student id = "))
        new_marks = int(input("Enter new marks = "))
        s.update_marks(student_id, new_marks)

    elif ch == "5":
        student_id = int(input("Enter student id = "))
        s.delete_student(student_id)

    elif ch == "6":
        break
    
    else:
        print("Invalid Choice")



    

