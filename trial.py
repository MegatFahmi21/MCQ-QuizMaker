import json
import os
import tkinter
import random


# #Main menu
# def main():
#     print("          MAIN MENU           ")
#     print(" ______________________________")
#     print("|1. Teacher registration      |")
#     print("|2. Student registration      |")
#     print("|3. Teacher log in            |")
#     print("|4. Student log in            |")
#     print("|_____________________________|")



# #TEACHER REGISTRATION

# def teacher():
#     name = input("Enter your name : ").upper()
#     age = input("Enter your age : ")
#     print("")
#     print("========================================================================")
#     print(f"Welcome {name}")
#     print(f"Your user ID is {random.randint(20000,29999)}")
#     password = input("Please set your password: ")
#     # Data to be written
#     dictionary ={
#     "name" : name,
#     "age" : age,
#     "ID" : f'{random.randint(20000,29999)}',
#     "password" : password
#     }
#     # Serializing json 
#     json_object = json.dumps(dictionary, indent = 4)
#     # Writing to sample.json
#     with open("teacher.json", "w") as outfile:
#         outfile.write(json_object)


# #Teacher Login
# def login():
#     user = input("Username : ")
#     passw = input("Password : ")

#     flag = True
#     with open("teacher.json") as f:
#         data = json.load(f)

#     while flag:
#         if passw == (data["password"]) and user == (data["ID"]):
#             print("ACCESS GRANTED")
#             flag = False
#         elif user == (data["ID"]) and passw != (data["password"]):
#             print("INCORRECT PASSWORD. TRY AGAIN")
#             passw = input("Password : ")
#         else:
#             print("THIS ACCOUNT IS NOT REGISTERED YET")
#             user = input("Username : ")
#             passw = input("Password : ")
# login()

# def inputs():
#     user_type = input("Enter the user type(student/teacher) : ").upper()

#     while True:
#         if user_type == "STUDENT":     
#             break
#         elif user_type == "TEACHER":
#             break
#         else:
#             a_input = input("TRY AGAIN. PRESS 'ENTER' TO CONTINUE")
#             clearScreen()
#             user_type = input("Enter the user type(student/teacher) : ").upper()

#     name = input("Enter your name : ").upper()




#     flag = True
#     while flag:
#         try:
#             age = int(input("Enter your age : "))
#             flag = False
#         except Exception as e:
#             print("ERROR : ONLY NUMBERS ARE ALLOWED")


#     password = input("Set your password : ")


#####DELETE STUDENT ACCOUNT
# def delete_student():
#     flag = True
#     while flag:
#         delete_q = input("Are you sure want to delete your account? (y/n) : ")
#         if delete_q == "y" or delete_q == "Y":
#             QUEST = input("YOUR ACCOUNT HAS BEEN DELETED. PRESS ENTER TO BACK TO MAIN MENU")
#             # Read student.json and store it in 'db_student'
#             with open('student.json', 'r') as f_student:
#                 db_student = json.load(f_student)

#             # # # Remove a person
#             del (db_student['students_det'][indeks])

#             # Write the updated 'db_student' to the student.json file
#             with open('student.json', 'w') as f_student:
#                 json.dump(db_student, f_student, indent=4)
#             clearScreen()
#             main()
#             flag = False
#         elif delete_q == "n" or delete_q == "N":
#             clearScreen()
#             home_stud()
#             flag = False
#         else:
#             print("TRY AGAIN> CLICK 'y' for yes or 'n' for no ")



#login system !!
# print(db_teacher["teachers_det"][-1])


# for i in db_student["students_det"]:
#     if 
# index = (db_student["students_det"]).index({'name': 'PRANJIVVAN', 'age': 16, 'ID': '15064', 'password': 'yjwrtgfb123'})
# print(index)
#print(i["ID"], i["password"])


# def login_s():
#     flag = True
#     while flag:
#         # Read student.json and store it in 'db_student'
#         with open('student.json', 'r') as f_student:
#             db_student = json.load(f_student)

#         user_ID = input("Enter your user ID : ")
#         user_pass = input("Enter your password :")

#         for i in (db_student["students_det"]):
#             if i["ID"] == user_ID and i["password"] == user_pass:
#                 print("ACCESS GRANTED")
      
      
#                 print(i["name"])
#                 flag = False
#             else:
#                 print("no")



#####DELETE TEACHER ACCOUNT
# def delete_teacher():
#     flag = True
#     while flag:
#         delete_q = input("Are you sure want to delete your account? (y/n) : ")
#         if delete_q == "y" or delete_q == "Y":
#             QUES = input("YOUR ACCOUNT HAS BEEN DELETED. PRESS ENTER TO BACK TO MAIN MENU")
            
#             # Read teacher.json and store it in 'db_teacher'
#             with open('teacher.json', 'r') as f_teacher:
#                 db_teacher = json.load(f_teacher)

#             # # # Remove a new person
#             del (db_teacher['teachers_det'][index])

#             # Write the updated 'db_teacher' to the teacher.json file
#             with open('teacher.json', 'w') as f_teacher:
#                 json.dump(db_teacher, f_teacher, indent=4)
#             clearScreen()
#             main()
#             flag = False
#         elif delete_q == "n" or delete_q == "N":
#             clearScreen()
#             home()
#             flag = False
#         else:
#             print("TRY AGAIN> CLICK 'y' for yes or 'n' for no ")



# # Read teacher.json and store it in 'db_teacher'
# with open('teacher.json', 'r') as f_teacher:
#     db_teacher = json.load(f_teacher)
# index = (db_teacher["teachers_det"]).index(t_li[0])
# # # Remove a new person
# del (db_teacher['teachers_det'][index])

# # Write the updated 'db_teacher' to the teacher.json file
# with open('teacher.json', 'w') as f_teacher:
#     json.dump(db_teacher, f_teacher, indent=4)

# print(db_teacher['teachers_det'])







   
# dict_s = (s_li[0])
# # Read teacher.json and store it in 'db_teacher'
# with open('student.json', 'r') as f_student:
#     db_student = json.load(f_student)

# # # rEMOVE a new person
# db_student['students_det'].remove(dict_s)

# # Write the updated 'db_student' to the student.json file
# with open('student.json', 'w') as f_student:
#     json.dump(db_student, f_student, indent=4)



