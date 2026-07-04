
def add_student(students):
    name=input("enter student name:")
    roll=input("enter student roll no.:")
    marks=int(input("enter the student marks:"))
    stud={"name":name,"roll_no": roll, "marks":marks}
    students.append(stud)
def search_student(students):
    name=input("enter student name: ")
    for student in students:
        if name in student.values():
            print(student)
        
def get_students(students):
    print("name\t rollno\t marks")
    print("-------------------------------------")
    for student in students:
        for v in student.values():
            print(f"{v}", end="\t ")
        print()