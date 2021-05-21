import random
import json
import os
# # # https://pysimplegui.readthedocs.io/en/latest/
# # import PySimpleGUI as sg

# sg.Window(title= "hello world", layout=[[]] , margins=(150,150)).read()

#Clearscreen
def clearScreen():
	if os.name == "nt":
		os.system("cls")
	else:
		os.system("clear")


def teacher():
    # user_type = input("Enter the user type(student/teacher) : ").upper()

    # while True:
    #     if user_type == "STUDENT":     
    #         break
    #     elif user_type == "TEACHER":
    #         break
    #     else:
    #         a_input = input("TRY AGAIN. PRESS 'ENTER' TO CONTINUE")
    #         clearScreen()
    #         user_type = input("Enter the user type(student/teacher) : ").upper()

    name = input("Enter your name : ").upper()

    flag = True
    while flag:
        try:
            age = int(input("Enter your age : "))
            flag = False
        except Exception as e:
            print("ERROR : ONLY NUMBERS ARE ALLOWED")


    password = input("Set your password : ")


    dictionary_t ={
    "name" : name,
    "age" : age,
    "ID" : f'{random.randint(20000,29999)}',
    "password" : password
    }
    # Read teacher.json and store it in 'db_teacher'
    with open('teacher.json', 'r') as f_teacher:
        db_teacher = json.load(f_teacher)

    # Add a new person
    db_teacher['teachers_det'].append(dictionary_t)

    # Write the updated 'db_teacher' to the teacher.json file
    with open('teacher.json', 'w') as f_teacher:
        json.dump(db_teacher, f_teacher, indent=4)

    clearScreen()
    # print(db_teacher["teachers_det"][-1])
    lname = db_teacher["teachers_det"][-1]["name"]
    l_ID = db_teacher["teachers_det"][-1]["ID"]
    lpass = db_teacher["teachers_det"][-1]["password"]
    print(f"HELLO {lname}!!")
    print("YOUR TEACHER ACCOUNT HAD REGISTERED.")
    print(f'Your user ID is {l_ID} and your password is {lpass}')
    print("Use your ID and password given for login system")
    mainp = input("Press 'ENTER' to back to main page")
    clearScreen()
    main()




def student():
    # user_type = input("Enter the user type(student/teacher) : ").upper()

    # while True:
    #     if user_type == "STUDENT":     
    #         break
    #     elif user_type == "TEACHER":
    #         break
    #     else:
    #         a_input = input("TRY AGAIN. PRESS 'ENTER' TO CONTINUE")
    #         clearScreen()
    #         user_type = input("Enter the user type(student/teacher) : ").upper()

    name = input("Enter your name : ").upper()

    flag = True
    while flag:
        try:
            age = int(input("Enter your age : "))
            flag = False
        except Exception as e:
            print("ERROR : ONLY NUMBERS ARE ALLOWED")


    password = input("Set your password : ")



    dictionary_s ={
    "name" : name,
    "age" : age,
    "ID" : f'{random.randint(10000,19999)}',
    "password" : password
    }
    # Read student.json and store it in 'db_student'
    with open('student.json', 'r') as f_student:
        db_student = json.load(f_student)

    # Add a new person
    db_student['students_det'].append(dictionary_s)

    # Write the updated 'db_teacher' to the teacher.json file
    with open('student.json', 'w') as f_student:
        json.dump(db_student, f_student, indent=4)

    clearScreen()
    # print(db_teacher["teachers_det"][-1]) means print the last person name in json file
    lnames = db_student["students_det"][-1]["name"]
    l_IDs = db_student["students_det"][-1]["ID"]
    lpasses = db_student["students_det"][-1]["password"]
    print(f"HELLO {lnames}!!")
    print("YOUR STUDENT ACCOUNT HAD REGISTERED.")
    print(f'Your user ID is {l_IDs} and your password is {lpasses}')
    print("Use your ID and password given for login system")
    mainp = input("Press 'ENTER' to back to main page")
    clearScreen()
    main()

def logout():
    flag = True
    while flag:
        logout_q = input("Are you sure want to log out? (y/n) : ")
        if logout_q == "y" or logout_q == "Y":
            QUES = input("PRESS ENTER TO BACK TO MAIN MENU")
            clearScreen()
            main()
            flag = False
        elif logout_q == "n" or logout_q == "N":
            clearScreen()
            home()
            flag = False
        else:
            print("TRY AGAIN> CLICK 'y' for yes or 'n' for no ")


def logout_stud():
    flag = True
    while flag:
        logout_q = input("Are you sure want to log out? (y/n) : ")
        if logout_q == "y" or logout_q == "Y":
            QUES = input("PRESS ENTER TO BACK TO MAIN MENU")
            clearScreen()
            main()
            flag = False
        elif logout_q == "n" or logout_q == "N":
            clearScreen()
            home_stud()
            flag = False
        else:
            print("TRY AGAIN> CLICK 'y' for yes or 'n' for no ")


def logout_admin():
    flag = True
    while flag:
        logout_q = input("Are you sure want to log out? (y/n) : ")
        if logout_q == "y" or logout_q == "Y":
            QUES = input("PRESS ENTER TO BACK TO MAIN MENU")
            clearScreen()
            main()
            flag = False
        elif logout_q == "n" or logout_q == "N":
            clearScreen()
            admin()
            flag = False
        else:
            print("TRY AGAIN> CLICK 'y' for yes or 'n' for no ")

s_li = [] # use for store student's account to delete
def student_login():
    user_ID = ""     
    user_pass = ""
    attempt_count = 0
    attempt_limit = 3

    flag = True
    while flag:
        if attempt_count < attempt_limit:
            print("")
            user_ID = input("Enter your user ID : ")
            user_pass = input("Enter your password :")
            attempt_count += 1
            print("")
            print(f'LOGIN FAILED.You tried for {attempt_count} time' )
        else:
            flag = False
            print("")
            print("ACCESS DENIED")
            print("YOU ARE GIVEN 3 ATTEMPT ONLY")
            t = input("PRESS 'ENTER' TO BACK TO MAIN PAGE")
            clearScreen()
            main()
        # Read student.json and store it in 'db_student'
        with open('student.json', 'r') as f_student:
            db_student = json.load(f_student)

        for i in (db_student["students_det"]):
            if i["ID"] == user_ID and i["password"] == user_pass:
                dictionary_sind = {'name' : i["name"] , "age" : i["age"] , "ID" : i["ID"] , "password" : i["password"] }                
                s_li.append(dictionary_sind)
                indeks = (db_student["students_det"]).index(s_li[0])                 
                clearScreen()
                print("ACCESS GRANTED")
                print(f' Welcome {i["name"]} !!')
                def home_stud():
                    print("          <--HOME PAGE-->             ")
                    print(" _____________________________________")
                    print("|1. Show new quiz                     |")
                    print("|2. Show attempted quiz               |")
                    print("|3. Log out                           |")
                    print("|_____________________________________|")
                    Inputs = input("Enter : ")
                    if Inputs == "3":
                        logout_stud()
                
                home_stud()
                flag = False




t_li = [] # use for store teacher's account to delete
def teacher_login():
    tuser_ID = ""     
    tuser_pass = ""
    tattempt_count = 0
    tattempt_limit = 3

    flag = True
    while flag:
        if tattempt_count < tattempt_limit:
            print("")
            tuser_ID = input("Enter your user ID : ")
            tuser_pass = input("Enter your password :")
            tattempt_count += 1
            print("")
            print(f"LOGIN FAILED. You tried for {tattempt_count} time.")
        else:
            flag = False
            print("")
            print("ACCESS DENIED")
            print("YOU ARE GIVEN 3 ATTEMPT ONLY")
            t_l = input("PRESS 'ENTER' TO BACK TO MAIN PAGE")
            clearScreen()
            main()
        # Read teacher.json and store it in 'db_teacher'
        with open('teacher.json', 'r') as f_teacher:
            db_teacher = json.load(f_teacher)

        for i in (db_teacher["teachers_det"]):
            if i["ID"] == tuser_ID and i["password"] == tuser_pass:
                dictionary_tind = {'name' : i["name"] , "age" : i["age"] , "ID" : i["ID"] , "password" : i["password"] }
                t_li.append(dictionary_tind)
                index = (db_teacher["teachers_det"]).index(t_li[0]) 
                clearScreen()
                print("ACCESS GRANTED")
                print(f' Welcome {i["name"]}!!')
                #home()
                
                def home():
                    print("          <--HOME PAGE-->             ")
                    print(" _____________________________________")
                    print("|1. Create quiz                       |")
                    print("|2. Edit quiz                         |")
                    print("|3. Delete quiz                       |")
                    print("|4. Show own quiz                     |")
                    print("|5. Log out                           |")
                    print("|_____________________________________|")
                    inputs = input("Enter : ")
                    if inputs == "5":
                        logout()
                home()                 
                flag = False


def admin_login():
    a_user_ID = ""     
    a_user_pass = ""
    a_attempt_count = 0
    a_attempt_limit = 3

    flag = True
    while flag:
        if a_attempt_count < a_attempt_limit:
            print("")
            a_user_ID = input("Enter your user ID : ")
            a_user_pass = input("Enter your password :")
            a_attempt_count += 1
            print("")
            print(f"LOGIN FAILED. You tried for {a_attempt_count} time.")
        else:
            flag = False
            print("")
            print("ACCESS DENIED")
            print("YOU ARE GIVEN 3 ATTEMPT ONLY")
            t_l = input("PRESS 'ENTER' TO BACK TO MAIN PAGE")
            clearScreen()
            main()
        # Read teacher.json and store it in 'db_teacher'
        with open('teacher.json', 'r') as f_teacher:
            db_teacher = json.load(f_teacher)

        for i in (db_teacher["admin_det"]):
            if i["ID"] == a_user_ID and i["password"] == a_user_pass:
                clearScreen()
                print("ACCESS GRANTED")
                print(f' Welcome {i["name"]}!!')
                #home()
                def admin():
                    print("          <--HOME PAGE-->             ")
                    print(" _____________________________________")
                    print("|1. View all teachers                  |")
                    print("|2. View all students                  |")
                    print("|3. Delete a student                   |")
                    print("|4. Delete a teacher                   |")
                    print("|5. Log out                            |")
                    print("|______________________________________|")
                    input_a = input("Enter your choices : ")
                    if input_a == "5":
                        logout_admin()
                    elif input_a == "1":
                        view_teacher()
                    elif input_a == "2":
                        view_student()
                    elif input_a == "4":
                        delete_teacher()
                    elif input_a == "3":
                        delete_student()
                admin()                 
                flag = False




def view_teacher():
    # Read teacher.json and store it in 'db_teacher'
    with open('teacher.json', 'r') as f_teacher:
        db_teacher = json.load(f_teacher)

    # print(db_teacher["teachers_det"])
    count = 0
    for teacher in db_teacher["teachers_det"]:
        count += 1

        print(f'\nTeacher #{count}')
        print(f'-Name = {teacher["name"]}')
        print(f'-ID   = {teacher["ID"]}')
        print(f'-Age  = {teacher["age"]}')
        

    input_home = input("Press 'ENTER' to back to home page")
    clearScreen()
    admin()	







def view_student():
    # Read student.json and store it in 'db_student'
    with open('student.json', 'r') as f_student:
        db_student = json.load(f_student)

    # print(db_student["students_det"])
    count = 0
    for student in db_student["students_det"]:
        count += 1

        print(f'\nStudent #{count}')
        print(f'-Name = {student["name"]}')
        print(f'-ID   = {student["ID"]}')
        print(f'-Age  = {student["age"]}')	
    ins = input("Press 'ENTER' to back to home page")
    clearScreen()
    admin()


def admin():
    print("          <--HOME PAGE-->             ")
    print(" _____________________________________")
    print("|1. View all teachers                  |")
    print("|2. View all students                  |")
    print("|3. Delete a student                   |")
    print("|4. Delete a teacher                   |")
    print("|5. Log out                            |")
    print("|______________________________________|")
    input_a = input("Enter your choices : ")
    if input_a == "5":
        logout_admin()
    elif input_a == "1":
        view_teacher()
    elif input_a == "2":
        view_student()
    elif input_a == "4":
        delete_teacher()
    elif input_a == "3":
        delete_student()  

def delete_teacher():
    d_user_ID = ""     
    d_attempt_count = 0
    d_attempt_limit = 3

    flag = True
    while flag:
        if d_attempt_count < d_attempt_limit:
            print("")
            d_user_ID = input("Enter  ID : ")
            d_attempt_count += 1
            print("")
            print(f"ID not found.You tried for {d_attempt_count} time.")
        else:
            flag = False
            print("")
            print("ID IS NOT EXIST IN THE TEACHER DATABASE !!!")
            print("YOU ARE GIVEN 3 ATTEMPT ONLY")
            t_l = input("PRESS 'ENTER' TO BACK TO MAIN PAGE")
            clearScreen()
            admin()
        # Read teacher.json and store it in 'db_teacher'
        with open('teacher.json', 'r') as f_teacher:
            db_teacher = json.load(f_teacher)

        for i in (db_teacher["teachers_det"]):
            if i["ID"] == d_user_ID:
                x_dict = {'name' : i["name"] , "age" : i["age"] , "ID" : i["ID"] , "password" : i["password"] }
                index = (db_teacher["teachers_det"]).index(x_dict)  
                flag = True
                while flag:
                    clearScreen()
                    print("Confirmation")
                    quit_q = input(f"Are you sure want to delete {i['name']} from database? (y/n) : ")
                    if quit_q == "y" or quit_q == "Y":
                        del (db_teacher['teachers_det'][index])
                        print(f'{i["name"]} has been removed from teacher account')
                        QUES = input("PRESS ENTER TO BACK TO HOME")
                        # # Write the updated 'db_teacher' to the teacher.json file
                        with open('teacher.json', 'w') as f_teacher:
                            json.dump(db_teacher, f_teacher, indent=4)
                        clearScreen()
                        admin()
                        flag = False
                    elif quit_q == "n" or quit_q == "N":
                        clearScreen()
                        admin()
                        flag = False
                    else:
                        print("TRY AGAIN> CLICK 'y' for yes or 'n' for no ")

# def admin():
#     print("          <--HOME PAGE-->             ")
#     print(" _____________________________________")
#     print("|1. View all teachers                  |")
#     print("|2. View all students                  |")
#     print("|3. Delete a student                   |")
#     print("|4. Delete a teacher                   |")
#     print("|5. Log out                            |")
#     print("|______________________________________|")
#     input_a = input("Enter your choices : ")
#     if input_a == "5":
#         logout_admin()
#     elif input_a == "1":
#         view_teacher()
#     elif input_a == "2":
#         view_student()
#     elif input_a == "4":
#         delete_teacher()
#     elif input_a == "3":
#         delete_student()  


def delete_student():
    del_user_ID = ""     
    del_attempt_count = 0
    del_attempt_limit = 3

    flag = True
    while flag:
        if del_attempt_count < del_attempt_limit:
            print("")
            del_user_ID = input("Enter  ID : ")
            del_attempt_count += 1
            print("")
            print(f"ID not found.You tried for {del_attempt_count} time.")
        else:
            flag = False
            print("")
            print("ID IS NOT EXIST IN THE STUDENT DATABASE !!!")
            print("YOU ARE GIVEN 3 ATTEMPT ONLY")
            t_l = input("PRESS 'ENTER' TO BACK TO MAIN PAGE")
            clearScreen()
            admin()
        # Read student.json and store it in 'db_student'
        with open('student.json', 'r') as f_student:
            db_student = json.load(f_student)

        for i in (db_student["students_det"]):
            if i["ID"] == del_user_ID:
                y_dict = {'name' : i["name"] , "age" : i["age"] , "ID" : i["ID"] , "password" : i["password"] }
                index = (db_student["students_det"]).index(y_dict)  
                flag = True
                while flag:
                    clearScreen()
                    print("CONFIRMATION")
                    quit_ques = input(f"Are you sure want to delete {i['name']} from database? (y/n) : ")
                    if quit_ques == "y" or quit_ques == "Y":
                        del (db_student['students_det'][index])
                        print(f'{i["name"]} has been removed from student account')
                        QUES = input("PRESS ENTER TO BACK TO HOME")
                        # # Write the updated 'db_student' to the student.json file
                        with open('student.json', 'w') as f_student:
                            json.dump(db_student, f_student, indent=4)
                        clearScreen()
                        admin()
                        flag = False
                    elif quit_ques == "n" or quit_ques == "N":
                        clearScreen()
                        admin()
                        flag = False
                    else:
                        print("TRY AGAIN> CLICK 'y' for yes or 'n' for no ")


       
def admin():
    print("          <--HOME PAGE-->             ")
    print(" _____________________________________")
    print("|1. View all teachers                  |")
    print("|2. View all students                  |")
    print("|3. Delete a student                   |")
    print("|4. Delete a teacher                   |")
    print("|5. Log out                            |")
    print("|______________________________________|")
    input_a = input("Enter your choices : ")
    if input_a == "5":
        logout_admin()
    elif input_a == "1":
        view_teacher()
    elif input_a == "2":
        view_student()
    elif input_a == "4":
        delete_teacher()
    elif input_a == "3":
        delete_student()



def quit():
    flag = True
    while flag:
        quit_q = input("Are you sure want to quit? (y/n) : ")
        if quit_q == "y" or quit_q == "Y":
            QUES = input("PRESS ENTER TO QUIT")
            exit()
        elif quit_q == "n" or quit_q == "N":
            clearScreen()
            main()
            flag = False
        else:
            print("TRY AGAIN> CLICK 'y' for yes or 'n' for no ")







def home():
    print("          <--HOME PAGE-->             ")
    print(" _____________________________________")
    print("|1. Create quiz                       |")
    print("|2. Edit quiz                         |")
    print("|3. Delete quiz                       |")
    print("|4. Show own quiz                     |")
    print("|5. Log out                           |")
    print("|_____________________________________|")
    inputs = input("Enter : ")
    if inputs == "5":
        logout()


def home_stud():
    print("          <--HOME PAGE-->             ")
    print(" _____________________________________")
    print("|1. Show new quiz                     |")
    print("|2. Show attempted quiz               |")
    print("|3. Log out                           |")
    print("|_____________________________________|")
    Inputs = input("Enter : ")
    if Inputs == "3":
        logout()


#Main menu
def main():
    print("             MAIN MENU                ")
    print(" _____________________________________")
    print("|1. Teacher registration              |")
    print("|2. Student registration              |")
    print("|3. Teacher log in                    |")
    print("|4. Student log in                    |")
    print("|5. Administrator log in              |")
    print("|6. Quit                              |")
    print("|_____________________________________|")
    flag = True
    while flag:
        inp = input(" Enter number : ")
        if inp == "1":
            teacher()
            flag = False
        elif inp == "2":
            student()
            flag = False
        elif inp == "3":
            teacher_login()
            flag = False
        elif inp == "4":
            student_login()
            flag = False
        elif inp == "5":
            admin_login()
            flag = False
        elif inp == "6":
            quit()
            flag = False
        else:
            print("You only allowed to enter number from 1-6. Try again")


#main()

# b= random.randint(600000,699999)  for quiz ID
# print(b)

main()