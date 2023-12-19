from colored import fg, attr, bg
import csv
import os 
import random
import string

def new_user(file_user):
    print(f"{fg('black')}{bg('white')}New Username{attr('reset')}")
    #Ask the title of the todo
    newuser_name = input("Enter your name: ")
    newuser_pwd = input("Enter your password: ")
    user_exists = False
    with open (file_user, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row and row[0] == newuser_name and row[1] == newuser_pwd:
                user_exists = True
                print(f"{fg('black')}{bg('white')}Username [{newuser_name}] already exists. Choose option 2 to login.{attr('reset')}")
                break
        if not user_exists:
            with open(file_user, "a", newline="") as f:
                writer = csv.writer(f)
                writer.writerow([newuser_name, newuser_pwd])
                print(f"{fg('black')}{bg('white')}Username [{newuser_name}] created! Choose option 2 to login.{attr('reset')}")

def user(user_list):
    user_list = "list.csv"
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
            if not os.path.exists("list.csv"):
                 print("No existing passwords, Please press 2 to create some!")
                 continue
            file = open(user_list)
            data = list(csv.reader(file, delimiter=","))

            # flat_data = [item for sublist in data for item in sublist]

            for item in data:
                print(item)
        elif user_choice == "2":
            print(f"{fg('black')}{bg('white')}Add a Password{attr('reset')}")
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
                    gen_pass_true = True
                    while gen_pass_true:
                        print(f"{fg('black')}{bg('white')}Generate a Password{attr('reset')}")
                        gen_username = input("Please create username for password: ")
                        pwd_gen = input(f"Would you like to generate a Password for {gen_username}? Y/N:  ")
                        
                        if pwd_gen == "Y":
                            generated_password = ''.join(random.choices(string.ascii_letters + string.digits, k=12))
                            print(f"{fg('black')}{bg('white')}Password Generated for {gen_username}: {generated_password}{attr('reset')}")

                            while True:
                                print("Would you like to save this password?   Y/N")
                                gen_input = input("Enter your selection: ")

                                if gen_input == "Y":
                                    with open(user_list, "a") as f:
                                        writer = csv.writer(f)
                                        writer.writerow([gen_username, generated_password])
                                    print(f"{fg('black')}{bg('white')}Password saved for {gen_username}!{attr('reset')}")
                                    gen_pass_true = False
                                    break

                                elif gen_input == "N":
                                    break
                                else:
                                     print("Invalid entry. Please enter Y or N.")
                            #if gen_input == "1", Save username & password, open cvs file and then store
                            #else, run password_gen function again
                            # break
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
            delete_name = ""
            delete_pwd = ""
            print("You entered 3")
            print(f"{fg('black')}{bg('white')}Delete a Password{attr('reset')}")
            password_delete(user_list, delete_name, delete_pwd)
        elif user_choice == "4":
            print(f"{fg('black')}{bg('white')}Main Menu {attr('reset')}")
            show_menu = False

def password_list(user_list):
    print(f"{fg('black')}{bg('white')}Creating a Password{attr('reset')}")
    #Ask the title of the todo
    pwd_name = input("Enter the name: ")
    pwd_pwd = input("Enter the password: ")
    # validate_user(file_user, newuser_name, newuser_pwd)
    # Insert that value into the file - list.csv (use WITH statment, it opens the file, appends and closes it in one go)
    with open(user_list, "a") as f:
        writer = csv.writer(f)
        writer.writerow([pwd_name, pwd_pwd])
    print(f"{fg('black')}{bg('white')}{pwd_name}'s password added! \nChoose option 1 to view them.{attr('reset')}")

def password_delete(user_list, delete_name, delete_pwd):
    delete_name = input("Enter the name of the password you would like to delete: ")
    delete_pwd = input("Enter the password: ")
    delete_sure = input(f"Are you sure you want to delete {delete_name}? (Y/N): ")
    if delete_sure == "Y":
        with open(user_list, 'r', newline='') as file:
                    # Read existing data from the CSV file
                    reader = csv.reader(file)
                    data = [row for row in reader]
                    


        with open(user_list, 'w', newline='') as file:
                    writer = csv.writer(file)
                    found_match = False
                    for row in data:
                        if row[0] != delete_name or row[1] != delete_pwd: 
                            writer.writerow(row)
                        else:
                            print(f"{fg('black')}{bg('white')}[{delete_name}] has been deleted successfully!{attr('reset')}")

                            found_match = True  # Set the variable to True, indicating a match
                    if not found_match:
                            print(f"{fg('black')}{bg('white')}Either [{delete_name}] doesn't exist or wrong password{attr('reset')}")

def password_gen(characters, length=15):
     #characters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "`","!","@","#","$","%","^","&","*"]
    # for loop, counter < 15, i++ increment)
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def store_password_in_csv(password, filename='generatedpasswords.csv'):
    with open(filename, 'a', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow([password])
        

character_list = [
    "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T",
    "U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n",
    "o","p","q","r","s","t","u","v","w","x","y","z", "0", "1", "2", "3", "4", "5", "6",
    "7", "8", "9","@","#","$","%","&","*"
]

generated_password = password_gen(character_list, length=15)
another_generated_password = password_gen(character_list, length=15)
store_password_in_csv(generated_password)
