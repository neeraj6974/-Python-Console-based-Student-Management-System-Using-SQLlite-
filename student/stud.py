import sqlite3

db = "./student.db"

con = sqlite3.connect(db)

cur = con.cursor()

def add_student(student_name , age , course , marks):
    cur.execute("""CREATE TABLE IF NOT EXISTS students(
    stud_id INTEGER PRIMARY KEY AUTOINCREMENT ,
    stud_name TEXT NOT NULL ,
    stud_age INTEGER NOT NULL ,
    stud_course TEXT NOT NULL ,
    marks INTEGER NOT NULL)""")

    cur.execute("""INSERT INTO students(stud_name, stud_age, stud_course, marks)
    VALUES(? , ? , ? , ?)""",(student_name , age , course , marks))

    con.commit()
    print("Student Added Successfully..!")

def display_student():
    cur.execute("SELECT * FROM students")

    record = cur.fetchall()

    for row in record:
        print(row)


def search_student(student_id):
    cur.execute("SELECT * FROM students WHERE stud_id = ?" , (student_id,))

    record = cur.fetchone()

    for row in record:
        print(row)
    

def update_marks(student_id , new_marks):

    cur.execute("UPDATE students SET marks = ? WHERE stud_id = ?" , (new_marks , student_id))

    con.commit()
    print("Marks Updated Successfully..!")

def delete_student(student_id):
    cur.execute("DELETE FROM students WHERE stud_id = ?" , (student_id,))
    print("Student Deleted Successfully..!")
    
    
    
