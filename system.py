import os
i=0





while i==0:
    print("-----------------Register System-----------------")
    question = input("1) New student enrollment \ n2) New teacher enrollment \ n3) Displays all students \ n4) Displays all teachers \ n5) Turn off the system:")
    if question == "1":
        print("-----------------Student Registration-----------------")
        students = open("students.txt", "a")
        name = input("Student Name:")
        lastname = input("Student Surname: ")
        schoolNumber = input("School number of the student: ")
        students.write("Name: " + name + " - Lastname: " + lastname + " - School Number: " + schoolNumber )
        students.close()
        os.system('cls' if os.name=='nt' else 'clear')
    if question == "2":
        print("-----------------Teacher Registration-----------------")
        teachers = open("teachers.txt", "a")
        name = input("Teacher name: ")
        lastname = input("Teacher surname:")
        branch = input("Teacher Branch:")
        teachers.write("Name: " + name + " - Lastname: " + lastname + " - Branch: " + branch + "\n")
        os.system('cls' if os.name=='nt' else 'clear')
    if question == "3":
        print("-----------------All Students-----------------")
        reads = open("students.txt")
        print(reads.read())
    if question == "4":
        print("-----------------All Teachers-----------------")
        readt = open("teachers.txt")
        print(readt.read())
    if soru == "5":
        break

    
