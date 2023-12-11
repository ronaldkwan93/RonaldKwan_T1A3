from colored import fg, attr, bg
from functions import new_user

user_list = "list.csv"
file_user = "users.csv"

print(f"{fg('black')}{bg('white')}Welcome to OnePWD Manager! {attr('reset')}")

try:
    # open the file in read mode
    todo_file = open(file_user, "r")
    todo_file.close()
    # print("In Try Block")
    # if it throws an error, it means the file doesn't exist
    # if no error, it means the file exists
except FileNotFoundError:
    # Now, we know the file doesn't exist
    # Create the file
    todo_file = open(file_user, "w")
    # We can also insert the first line into the file
    # todo_file.write("User, Password\n")  # /n means go to the next line entered
    todo_file.close()
    print("In except block")

def create_menu():
    print("1. Enter 1 if you are a new user")
    print("2. Enter 2 to login")
    print("5. Enter 5 to exit")
    choice = input("Enter your selection: ")
    return choice

users_choice = ""
user = ""
password = ""

while users_choice != "5":
    users_choice = create_menu()

    if users_choice == "1":
        print("You entered 1")
        new_user(file_user)
    elif users_choice == "2":
        # if user is validated, show user menu
        print(f"{fg('black')}{bg('white')}Login Authentication {attr('reset')}")
        user = input("Please insert your username: ")
        password = input("Please insert your password: ")
        
    elif users_choice == "5":
        continue  # user goes out of the loop to the print "Thank you" message
    else:
        print("Invalid Input")


print("Thank you for using OnePWD Manager!")

