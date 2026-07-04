
def calculate_average(students):
    addition=0
    count=0
    for stud in students:
        addition+=stud.get("marks")
        count+=1
    if count==0:
        print("none")
    else:
        avg=addition/count
        print(f"the average is {avg}")
def find_topper(students):
    topper=None
    topperinfo=None
    marks=highest_marks(students)
    for stud in students:
        if stud["marks"]==marks:
            topperinfo=stud
    print(topperinfo)
def highest_marks(students):
    high=0
    for stud in students:
        mark=stud.get("marks")
        if high<mark:
            high=mark
    return high 
