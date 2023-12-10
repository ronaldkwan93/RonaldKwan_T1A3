import csv


def new_user(file_user):
    print("New UserName")
    #Ask the title of the todo
    newuser_name = input("Enter your name: ")
    newuser_pwd = input("Enter your password: ")
    check_new_user(file_user, newuser_name, newuser_pwd)
    # Insert that value into the file - list.csv (use WITH statment, it opens the file, appends and closes it in one go)
    with open(file_user, "a") as f:
        writer = csv.writer(f)
        writer.writerow([newuser_name, newuser_pwd])

def user(file_user):
    print("1. Press 1 to view current passwords")
    print("2. Press 2 to add a password")
    print("3. Press 3 to delete a password")
    print("4. Press 4 to exit")
    user_choice = input("Enter your selection: ")
    users_choice = ""

    if user_choice == "1":
        print("You entered 1")
    elif user_choice == "2":
        print("You entered 2")
    elif user_choice == "3":
        print("You entered 3")
    elif user_choice == "4":
        print("This is working")


def check_new_user(file_user, newuser_name, newuser_pwd):
    
    with open(file_user, 'r') as file:
        csv_reader = csv.reader(file)
            
            # Assuming the input value is in the first column of the CSV file
        for row in csv_reader:
            if row and row[0] == newuser_name:
                print("You are already a user, Press 2 to login")
                return

