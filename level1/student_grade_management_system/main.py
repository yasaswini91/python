#using modules and functions
from student import *
from calculations import *
students=[]
def main():
    
    flag=True
    while flag:
        print("====== MENU ======")
        print("1 Add Student\n2 Search Student\n3 View Students\n4 Average Marks\n5 Topper\n6 Exit")
        n=None
        while n not in [1,2,3,4,5,6]:
            n=int(input("enter your choice: "))
        flag=choicetaken(n)
def choicetaken(choice):
    match choice:
        case 1: 
            add_student(students)
            return True
        case 2: 
            search_student(students)
            return True
        case 3: 
            get_students(students)
            return True
        case 4:
            calculate_average(students)
            return True
        case 5:
            find_topper(students)
            return True
        case 6: 
            print("exited")
            return False
main()