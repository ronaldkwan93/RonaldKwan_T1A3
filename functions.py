from colored import fg, attr, bg
import csv

def new_user(file_user):
    print("New UserName")
    #Ask the title of the todo
    newuser_name = input("Enter your name: ")
    newuser_pwd = input("Enter your password: ")
    # validate_user(file_user, newuser_name, newuser_pwd)
    # Insert that value into the file - list.csv (use WITH statment, it opens the file, appends and closes it in one go)
    with open(file_user, "a") as f:
        writer = csv.writer(f)
        writer.writerow([newuser_name, newuser_pwd])

def user(file_user):
    show_menu = True

    while show_menu:
        print("1. Press 1 to view current passwords")
        print("2. Press 2 to add a password")
        print("3. Press 3 to delete a password")
        print("4. Press 4 to exit back to main menu")
        user_choice = input("Enter your selection: ")
        users_choice = ""

        if user_choice == "1":
            print("You entered 1")
        elif user_choice == "2":
            print(f"{fg('black')}{bg('white')}Add a Password {attr('reset')}")
            print("Would you like to add a password manually? Press 1")
            print("Would you like the system to generate one? Press 2")
            add_pwd = input("Enter your selection: ")
            if add_pwd == "1": 
                manual_username = input("Please create username for password: ")
                manual_pwd = input(f"Please type in password for {manual_username}:  ")    
                print(f"{fg('black')}{bg('white')}Password added!{attr('reset')}")
        elif user_choice == "3":
            print("You entered 3")
            print("Please type the username of password to delete: ")
        elif user_choice == "4":
            print(f"{fg('black')}{bg('white')}Main Menu {attr('reset')}")
            show_menu = False


# def validate_user(file_path):
#     input_username = input("Enter your username: ")
#     input_password = input("Enter your password: ")
    
#     with open(file_path, mode='r') as file:
#         csv_reader = csv.reader(file)
#         for row in csv_reader:
#             if row and len(row) >= 2 and row[0] == input_username and row[1] == input_password:
#                 return True
#     return False

# file_user = "users.csv"

# if validate_user(file_user):
#     print("Validation successful. User found in the CSV file.")
# else:
#     print("Validation failed. User not found or incorrect credentials.")


