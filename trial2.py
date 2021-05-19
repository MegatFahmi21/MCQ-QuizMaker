
#demo 1 - Create a student "database" application
#       - (without using the concept of object)

# How to store a student data?
#Assume that a student has an ID, a name and an age

#Demo 1:
#https://codeshare.io/5M0Jrq

# Demo 1 (Add a new student):
# https://codeshare.io/5M0Jdq

# Student.py:
# https://codeshare.io/G74081

# Student.py (version 2)
# https://codeshare.io/ad7jeZ

# Demo 3:
# https://codeshare.io/5zD9Xr

# names = [
#     "William", "Justin", "Donald"
# ]


# ids = [
#     '11111', '22222', '33333'
# ]

# ages = [
#     100, 3, 1234
# ]


# def menu():
#     print('----Menu----')
#     print("1.View all students")
#     print("2. Add a student")
#     print("3. Delete a student")
#     print('0. EXIT')
#     return int(input("Enter your choices : "))
# #create a program that allows user to interact with student "database"
# while True:
#     os.system("cls")
#     choice == menu()
#     if choice == 0:
#         break

# print

import PySimpleGUI as sg
import json


	
sg.theme('BluePurple')

layout = [[sg.Text('Enter your name :')],
		[sg.Input(key='-IN1-')],
		[sg.Text('Enter your password :')],
		[sg.Input(key='-IN2-')],
		[sg.Button('Login', size=(40,1), pad=(10,10))],
        [sg.Text(size=(20,1), key='-OUTPUT-')]]

window = sg.Window('Student Log In System', layout)

# Read student.json and store it in 'db_student'
with open('student.json', 'r') as f_student:
	db_student = json.load(f_student)
while True:
	event, values = window.read()
	print(event, values)
	
	if event == None:
		break
	
	if event == 'Login':
		# Update the "output" text element
		# to be the value of "input" element
		# window['-OUTPUT-'].update("Welcome" + " " +  values['-IN1-'])		
		for student in db_student["students_det"]:
			if values["-IN1-"] == student["name"] and values["-IN2-"] == student["password"]:
				# window['-OUTPUT-'].update(f"Welcome {student['name']}")
				print("ACCESS GRANTED")
				window['-OUTPUT-'].update(f"Welcome {values['-IN1-']}")
			else:
				window['-OUTPUT-'].update("NAME NOT FOUND")

				     
        
window.close()

# a = input("Enter:")
# b = input("Enter:")

# for student in db_student["students_det"]:
# 	if a == student["ID"] and b == student["password"]:
# 		print(f'{student["name"]}')




