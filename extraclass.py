#==========================================================================================================
#Final Demo:
#https://codeshare.io/24zKNE


##### Python Tkinter Import Statements #####
import tkinter as tk 		# tk = tkinter
import tkinter.ttk as ttk	# ttk = themed tkinter

##### Setup Main Application Window #####
# Create a main application window using tkinter class constructor
root = tk.Tk() 
root.title('Login Screen')
root.geometry('300x150') # Set the width and height to 300 and 150 respectively

##### UI Widgets #####
lbl_title = ttk.Label(root, text='Taco Bell\'s Login Screen')
lbl_username = ttk.Label(root, text='Username:')
lbl_password = ttk.Label(root, text='Password:')

ent_username = ttk.Entry(root)
ent_password = ttk.Entry(root)

btn_login = ttk.Button(root, text='Login')

##### UI Layouts #####

# We are using Grid Geometry Manager as the layout formula
lbl_title.grid(row=0, column=0, columnspan=2)
lbl_username.grid(row=1, column=0)
ent_username.grid(row=1, column=1)
lbl_password.grid(row=2, column=0)
ent_password.grid(row=2, column=1)
btn_login.grid(row=3, column=0, columnspan=2, sticky=tk.NSEW)

##### UI Behaviours #####
db_user_account = [
	  {'username':'justin', 'password':'bieber'}
	, {'username':'selena', 'password':'gomez'}
	, {'username':'donald', 'password':'trump'}
]

# Set the btn_login's 'command' option to a function that
# will be executed when btn_login is clicked
def verify_user():
	print('Login button clicked')

	# Get the input username and password from the corresponding Entry(s)
	input_username = ent_username.get()
	input_password = ent_password.get()

	# Task: Search through the user account database
	#	    Decide if the login is successful or failed
	# Change the following:

	# Option 1: Most traditional approach
	# found_user = False
	# for account in db_user_account:
	# 	if input_username == account['username'] and input_password == account['password']:
	# 		print('Login Successful')
	# 		found_user = True
	# 		break
	
	# if not found_user:
	# 	print('Login Failed')

	# Option 2: Use for-else block
	for account in db_user_account:
		if input_username == account['username'] and input_password == account['password']:
			print('Login Successful')
			break
	else:
		print('Login Failed')

btn_login['command'] = verify_user

##### Run GUI Application #####
root.mainloop()