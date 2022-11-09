#=====importing libraries===========
# This import allows the program to access the date functions which
# will be used to access the current date.
import datetime 

# The passw and user variables are used to store the values from the file.
# The username and password variables are used to store the user input.
# The set_password boolean is used for the loop that checks whether the user has entered
# the correct password.
# The current_date variable stores current date
passw = ""
user = ""
username = ""
password = ""
set_password = True
current_date = datetime.datetime.now()

#====Login Section====
# This opens the user.txt file with read permissions.
# The newline characters are replaced with commas and the spaces are replaced with nothing and stored in the user variable.
# This variable is then split by commas and stored in a variable called credentials making them easier to access later.
# The usernames are stored in a user variable by slicing the credentials variable starting at the first index position and
# stepping through every two elements to match the format the usernames are stored in the user.txt file.
# The passwords are stored in a passw variable by slicing the credentials variable starting at the second index position and
# stepping through every two elements to match the format the passwords are stored in the user.txt file.
with open('user.txt', 'r+') as f:
    for line in f:
        user += line
        user = user.replace('\n', ',')
        user = user.replace(' ', '')
    credentials = user.split(",") 
    user = credentials[0::2]
    passw = credentials[1::2]

#!!!!Remove!!!!
print(user)
print(passw)
#!!!!Remove!!!!
 
 # This loop is used to repeatedly check whether the user has entered the correct username by comparing the user enters with what
 # is stored in the username variable. If they do not match the user is asked to try again
for name in user:
    username = input("\nPlease enter your username: ")
    if username in user:
        print("Your username is correct")
        break
    else:
        print("You username is incorrect, please try again.")

 # This loop is used to repeatedly check whether the user has entered the correct password by comparing what the user enters with what
 # is stored in the password variable. If they do not match the user is asked to try again
for passphrase in user:
    password = input("Please enter your password: ")
    if password in passw:
        print("Your password is correct")
        break
    else:
        print("Your password is incorrect")

'''Here you will write code that will allow a user to login.
    - Your code must read usernames and password from the user.txt file
    - You can use a list or dictionary to store a list of usernames and passwords from the file.
    - Use a while loop to validate your user name and password.
'''

while True:
    # Presenting the menu to the user and 
    # making sure that the user input is converted to lower case.
    menu = input('''\nSelect one of the following Options below:
    r - Registering a user
    a - Adding a task
    va - View all tasks
    vm - view my task
    e - Exit
    : ''').lower()

    # If the user selects option r in the menu the user is prompted to add a new user
    if menu == 'r':
        # While the set_password variable is set to True, the user is asked to enter the new users, username and password. They are
        # asked to confirm the password.
        while set_password:
            new_username = input("Please enter the new username: ")
            new_password = input("Please enter the new password: ")
            confirm_password = input("Please re-enter the new password: ")

            # If both entries of the password match, the username and password are stored in a variable called new_credentials with a
            # comma appended to the end of the username and a space before the new password to maintain the same format in the text file.
            if confirm_password == new_password:
                new_credentials = new_username + ","
                new_credentials += " " + new_password
                set_password = False

                #!!!!Remove!!!!
                print(new_credentials)
                #!!!!Remove!!!!

                # This write the new_credentials variable into the user.txt file. If the passwords do not match then the user is asked to
                # start over from entering the username.
                with open('user.txt', 'a') as f:
                    f.write('\n' + new_credentials)
            else:
                print("The passwords do not match please try again: ")

        
        '''In this block you will write code to add a new user to the user.txt file
        - You can follow the following steps:
            - Request input of a new username
            - Request input of a new password
            - Request input of password confirmation.
            - Check if the new password and confirmed password are the same.
            - If they are the same, add them to the user.txt file,
            - Otherwise you present a relevant message.'''

    # If the user selects option a in the menu the user is prompted to add a new task
    elif menu == 'a':
        # The user is asked to enter: who the task is assigned to, the title, the task description, the task date and the current date.
        # This information is then appended into relevant variables
        task_user = input("Who is this task assigned to: ")
        title = input("What is the title for this task: ")
        task_desc = input("What is the description of this task: ")
        task_date = input("What is the due date for this task: ")
        current_date = current_date.strftime('%d %b %y')

        # Below the variables are added to the new_task variable adding commas and spaces to maintain the same format in the tasks.txt
        new_task = task_user + (',')
        new_task += (' ') + title + (',')
        new_task += (' ') + task_desc + (',')
        new_task += (' ') + task_date + (',')
        new_task += (' ') + current_date + (',')
        new_task += (' ') + 'No'
        
        # The tasks.txt file is opened with append permissions which allows new elements to be added to the bottom of the file
        # The new_task variable is written to the tasks.txt file
        with open('tasks.txt', 'a') as f:
            f.write('\n' + new_task)


        '''In this block you will put code that will allow a user to add a new task to task.txt file
        - You can follow these steps:
            - Prompt a user for the following: 
                - A username of the person whom the task is assigned to,
                - A title of a task,
                - A description of the task and 
                - the due date of the task.
            - Then get the current date.
            - Add the data to the file task.txt and
            - You must remember to include the 'No' to indicate if the task is complete.'''

    elif menu == 'va':
        pass
        '''In this block you will put code so that the program will read the task from task.txt file and
         print to the console in the format of Output 2 presented in the L1T19 pdf file page 6
         You can do it in this way:
            - Read a line from the file.
            - Split that line where there is comma and space.
            - Then print the results in the format shown in the Output 2 in L1T19 pdf
            - It is much easier to read a file using a for loop.'''

    elif menu == 'vm':
        pass
        '''In this block you will put code the that will read the task from task.txt file and
         print to the console in the format of Output 2 presented in the L1T19 pdf
         You can do it in this way:
            - Read a line from the file
            - Split the line where there is comma and space.
            - Check if the username of the person logged in is the same as the username you have
            read from the file.
            - If they are the same you print the task in the format of output 2 shown in L1T19 pdf '''

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")