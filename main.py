import csv
from colored import fg, attr, bg
from functions import new_user, user

BLUE = '\033[94m'
user_list = "list.csv"
file_user = "users.csv"
ascii_art = '''
 ____ ____ ____ ____ ____ ____ _________ ____ ____ ____ ____ ____ ____ ____ 
||o |||n |||e |||P |||W |||D |||       |||M |||a |||n |||a |||g |||e |||r ||
||__|||__|||__|||__|||__|||__|||_______|||__|||__|||__|||__|||__|||__|||__||
|/__\|/__\|/__\|/__\|/__\|/__\|/_______\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|
'''
login_art = '''
 ____ ____ ____ ____ ____ 
||L |||O |||G |||I |||N ||
||__|||__|||__|||__|||__||
|/__\|/__\|/__\|/__\|/__\|
'''
mainmenu_art = '''
____ ____ ____ ____ _________ ____ ____ ____ ____ 
||M |||A |||I |||N |||       |||M |||E |||N |||U ||
||__|||__|||__|||__|||_______|||__|||__|||__|||__||
|/__\|/__\|/__\|/__\|/_______\|/__\|/__\|/__\|/__\|
'''
about_art = '''
 ____ ____ ____ ____ _________ ____ ____ _________ ____ ____ ____ ____ ____ ____ ____ 
||W |||H |||A |||T |||       |||I |||S |||       |||O |||N |||E |||P |||W |||D |||? ||
||__|||__|||__|||__|||_______|||__|||__|||_______|||__|||__|||__|||__|||__|||__|||__||
|/__\|/__\|/__\|/__\|/_______\|/__\|/__\|/_______\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|
'''

print(f"{fg('blue')}{bg('black')}Welcome to: {attr('reset')}")
print(ascii_art)
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
    with open(file_user, "a") as f:
                        writer = csv.writer(f)
                        writer.writerow(["Admin", "Admin"])
    # print("In except block")

def create_menu():
    print(" Enter 1 if you are a new user")
    print(" Enter 2 to login")
    print(" Enter 3 for FAQs")
    print(" Enter 5 to exit")
    choice = input("Enter your selection: ")
    return choice

users_choice = ""
password = ""

while users_choice != "5":
    users_choice = create_menu()

    if users_choice == "1":
        print("You entered 1")
        new_user(file_user)
    elif users_choice == "2":
        print(login_art)
        # if user is validated, show user menu
        user_name = input("Enter your username: ")
        user_pass = input("Enter your password: ")
        with open(file_user, 'r', newline='') as file:
                    # Read existing data from the CSV file
                    reader = csv.reader(file)
                    validation_user = False
                    username_not_found = True
                    data = [row for row in reader]
                    for row in data:
                        if row[0] == user_name and row[1] == user_pass: 
                            print(f"{fg('green')}{bg('black')}Login Success!{attr('reset')}")
                            print(f"{fg('blue')}{bg('black')}Hello [{user_name}], Welcome back!{attr('reset')}")
                            print(mainmenu_art)
                            validation_user = True
                            user(user_list)
                            username_not_found = False
                            break

                    if username_not_found:
                            print(f"{fg('yellow')}{bg('black')}[Error] [{user_name}] is not a valid username or wrong password! Please try again!{attr('reset')}")
                         
    elif users_choice == "3":
        print(about_art)
        print(f"{fg('blue')}{bg('black')}About ONEPWD{attr('reset')}")
        print("Welcome to ONEPWD MANAGER, a secure and user-friendly password management solution designed to keep your online accounts safe and easily accessible. This password manager is built with a focus on privacy, encryption, and simplicity.")
        print("\n")
        print(f"{fg('Green')}Features:{attr('reset')}")
        print("**Login creation:** To access your password vault safely")
        print("**Add and Organise Passwords:** Safely store your login credentials for different websites and services.")
        print("**Password Generator:** Generate strong passwords for new accounts or password updates.")
        print("**Security First:** Regularly scans your made passwords and gives it a security rating (from very weak to strong), to protect your system better.")
        print("**Reports:** Providing an overview of your total created passwords and time of when you logged in last, total transparency.")
        print("\n")
        print("Your security is our top priority. ONEPWD MANAGER does not store your master password or any of your decrypted passwords, ensuring that only you have access to your sensitive information.")
        print("\n")
        print("Thank you for choosing ONEPWD MANAGER for your password management needs. If you have any questions or feedback, please contact us at support@ONEPWD.com.")
        print("Stay secure, \nThe ONEPWD Team")
        print("\n")
    elif users_choice == "5":
        continue  # user goes out of the loop to the print "Thank you" message
    else:
        print("Invalid Input")


print(f"{fg('blue')}{bg('black')}Thank you for using OnePWD Manager! See you soon!{attr('reset')}")

