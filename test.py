from enum import Enum
import os


students = []

FILENAME = "STUDENTS.txt"


class options(Enum):
    ADD = 1
    EXIT = 2
    SHOW_STUDENTS = 3


def menue():

    while True:
        clear_screen()
        useroptions()
        userselection = options(int(input("your selection - ")))
        if userselection == options.ADD:
            addnewstudent()
        if userselection == options.EXIT:
           clear_screen(),exitandsave()
        if userselection == options.SHOW_STUDENTS:
           clear_screen(),show_students(),input("press enter to show the menue")

        
        

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def useroptions():
    for useroption in options:
        print(useroption.name, "-", useroption.value)


def show_students():
    for student in students:
        print(student)  


def exitandsave():
    with open(FILENAME, 'w') as file:
        for student in students:
            file.write(f"{student.strip()}\n")
    print("File written successfully")
    exit()


def readfile():
    global students
    try:
        with open(FILENAME, "r") as studfile:
            students = [line.strip()
                        for line in studfile]  
    except FileNotFoundError:
        print("File not found. Starting with an empty list.")

    except:
        FileNotFoundError


def addnewstudent():
    newstudent = input("student name - ")
    students.append(newstudent)
    print("student added")
    clear_screen()



if __name__ == "__main__":
    readfile()
    menue()
