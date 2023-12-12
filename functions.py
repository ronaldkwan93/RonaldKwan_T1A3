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
    print(f"{fg('black')}{bg('white')}Welcome {newuser_name}! \nChoose option 2 to login.{attr('reset')}")

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
            print(f"{fg('black')}{bg('white')}Current Passwords (Name, Password){attr('reset')}")
            # view_pwd = input("Please type in your User Password: ")
            file = open("list.csv")
            data = list(csv.reader(file, delimiter=","))
            file.close()

            flat_data = [item for sublist in data for item in sublist]

            for item in data:
                print(item)
        elif user_choice == "2":
            print(f"{fg('black')}{bg('white')}Add a Password {attr('reset')}")
            while True:
                print("1. Press 1 to add a password manually")
                print("2. Press 2 to generate a secure password")
                print("3. Press 3 to go back to Main menu")
                add_pwd = input("Enter your selection: ")
                if add_pwd == "1": 
                    user_list = "list.csv"
                    password_list(user_list)
                    break
                elif add_pwd == "2":
                    print(f"{fg('black')}{bg('white')}Generate a Password{attr('reset')}")
                    gen_username = input("Please create username for password: ")
                    pwd_gen = input(f"Would you like to generate a Password for {gen_username}? Y/N:  ")
                    if pwd_gen == "Y":
                        print(f"Password Generated for {gen_username}:  ")
                        print("Would you like to save this password? Option 1")
                        print("Would you like a different generated password? Option 2")
                        gen_input = input("Enter your selection: ")
                        break
                    elif pwd_gen == "N":
                        print(f"{fg('black')}{bg('white')}User Menu{attr('reset')}")
                        break
                    else:
                        print("Invalid selection! Please enter Y/N")
                elif add_pwd == "3":
                    print(f"{fg('black')}{bg('white')}User Menu{attr('reset')}")
                    break
                else:
                    print("Invalid selection! Please enter 1, 2, 3")

        elif user_choice == "3":
            print("You entered 3")
            print(f"{fg('black')}{bg('white')}Delete a Password{attr('reset')}")
            pwd_delete = input("Please type the username of password to delete: ")
        elif user_choice == "4":
            print(f"{fg('black')}{bg('white')}Main Menu {attr('reset')}")
            show_menu = False

def password_list(user_list):
    print("New UserName")
    #Ask the title of the todo
    pwd_name = input("Enter the name: ")
    pwd_pwd = input("Enter the password: ")
    # validate_user(file_user, newuser_name, newuser_pwd)
    # Insert that value into the file - list.csv (use WITH statment, it opens the file, appends and closes it in one go)
    with open(user_list, "a") as f:
        writer = csv.writer(f)
        writer.writerow([pwd_name, pwd_pwd])
    print(f"{fg('black')}{bg('white')}{pwd_name}'s password added! \nChoose option 1 to view them.{attr('reset')}")

