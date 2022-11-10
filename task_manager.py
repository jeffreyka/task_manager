#=====importing libraries===========
# This import allows the program to access the date functions which
# will be used to access the current date.
import datetime 

# The passw and user variables are used to store the values from the file.
# The username and password variables are used to store the user input.
# The all_tasks variable stores the contents of the tasks.txt file.
# the number_of_tasks and number_of_users variables are counters store an int.
# The set_password boolean is used for the loop that checks whether the user has entered
# the correct password.
# The current_date variable stores current date.
passw = ""
user = ""
username = ""
password = ""
all_tasks = ""
number_of_tasks = 0
number_of_users = 0
set_password = True
login = True
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
 
 # This loop is used to repeatedly check whether the user has entered the correct username by comparing the user enters with what
 # is stored in the username variable. If they do not match the user is asked to try again.
while login:
    username = input("\nPlease enter your username: ")
    if username in user:
        print("Your username is correct")
        login = False
    else:
        login = True
        print("You username is incorrect, please try again.")

 # This loop is used to repeatedly check whether the user has entered the correct password by comparing what the user enters with what
 # is stored in the password variable. If they do not match the user is asked to try again.

login = True

while login:
    password = input("Please enter your password: ")
    if password in passw:
        print("Your password is correct")
        login = False
    else:
        print("Your password is incorrect")
        login = True

while True:
    if username == 'admin':
        # Presenting the menu to the user and 
        # making sure that the user input is converted to lower case.
        # A new menu option is added if the user has logged in as the admin user.
        menu = input('''\nSelect one of the following Options below:
        r - Registering a user
        a - Adding a task
        va - View all tasks
        vm - view my task
        s - View statictics
        e - Exit
        : ''').lower()
    
    else:
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
        if username != 'admin':
            print("Sorry you must be logged in as admin to complete this action.")
            continue
        
        else:
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

                    # This write the new_credentials variable into the user.txt file. If the passwords do not match then the user is asked to
                    # start over from entering the username.
                    with open('user.txt', 'a') as f:
                        f.write('\n' + new_credentials)
                else:
                    print("The passwords do not match please try again: ")

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

    # If the user selects option va in the menu the user is shown all the tasks on the file
    elif menu == 'va':

        # This opens the task.txt file with read/write permissions
        with open('tasks.txt', 'r+') as f:
            # This loop adds each line from the text file with a newline character to a variable called all_tasks
            #  and prints all the tasks to the user
            for line in f:
                all_tasks += line + ("\n")
            print(all_tasks)

    # If the user selects option vm in the menu the user is shown all the tasks assigned to them from the file
    elif menu == 'vm':
        # This opens the task.txt file with read/write permissions
        with open('tasks.txt', 'r+') as f:
             # This loop adds each line from the text file to a variable called my_task
            #  If the the current user's username is in the current line of the loop that
            for line in f:
                if username in line:
                    print(line)
    
    # If the admin selects option s in the menu the user is shown the count of all users and all tasks
    elif menu == 's':
        # This opens the task.txt file with read/write permissions
        with open('tasks.txt', 'r+') as f:
            # This loop will add 1 to the number_of_tasks variable for every line in the tasks.txt
            for line in f:
                number_of_tasks += 1
        
        # This opens the task.txt file with read/write permissions
        with open('user.txt', 'r+') as f:
            # This loop will add 1 to the number_of_users variable for every line in the tasks.txt
            for line in f:
                number_of_users += 1
        
        # This will print the total amount of tasks and users
        print(f"\nThere are {number_of_users} users and {number_of_tasks} tasks.")

    # If the user selects option e in the menu the goodbye message is displayed and the program ends
    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    # If at the selection stage the user hasn't selected an option from the menu but entered something else they are prompted
    # to try again and the loop interates
    else:
        print("You have made a wrong choice, Please Try again")