import os
i=0





while i==0:
    print("-----------------Kayıt Sistemi-----------------")
    soru = input("1) Yeni öğrenci kaydı \n2) Yeni öğretmen kaydı \n3) Tüm öğrencileri Gösterir\n4) Tüm öğretmenleri gösterir\n5) Sistemi kapat: ")
    if soru == "1":
        print("-----------------Öğrenci Kayıt-----------------")
        students = open("students.txt", "a")
        name = input("Öğrenci Adı: ")
        lastname = input("Öğrenci Soyadı: ")
        schoolNumber = input("Öğrencinin okul numarası: ")
        students.write("Ad: " + name + " - Soyadı: " + lastname + " - Okul numarası: " + schoolNumber + "\n")
        students.close()
        os.system('cls' if os.name=='nt' else 'clear')
    if soru == "2":
        print("-----------------Öğretmen Kayıt-----------------")
        teachers = open("teachers.txt", "a")
        name = input("Öğretmen Adı: ")
        lastname = input("Öğretmen Soyadı: ")
        branch = input("Öğretmenin Branşı: ")
        teachers.write("Ad: " + name + " - Soyadı: " + lastname + " - Branşı: " + branch + "\n")
        os.system('cls' if os.name=='nt' else 'clear')
    if soru == "3":
        print("-----------------Tüm Öğrenciler-----------------")
        reads = open("students.txt")
        print(reads.read())
    if soru == "4":
        print("-----------------Tüm Öğretmenler-----------------")
        readt = open("teachers.txt")
        print(readt.read())
    if soru == "5":
        break

    