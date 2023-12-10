import csv


def new_user(file_user):
    print("New UserName")
    #Ask the title of the todo
    newuser_name = input("Enter your name: ")
    newuser_pwd = input("Enter your password: ")
    # Insert that value into the file - list.csv (use WITH statment, it opens the file, appends and closes it in one go)
    with open(file_user, "a") as f:
        writer = csv.writer(f)
        writer.writerow([newuser_name, newuser_pwd])
    # while inserting - Title = user entered
                    # - completed = False

def remove_todo(file_name):
    print("Remove todo")
    todo_name = input("Enter a todo that you want to remove: ")
    # copy all the contents of the csv into a new csv
    # while doing this, we constantly check for the condition
    # when we encounter todo to be removed, we don't copy that one
    # the final new todo will be written in the csv file 
    todo_lists = []
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if (todo_name != row[0]):
                todo_lists.append(row)
    with open(file_name, "w") as f:
        writer = csv.writer(f)
        writer.writerows(todo_lists)

def mark_todo(file_name):
    print("Mark todo")
    todo_name = input("Enter the todo name that you want to makr as complete: ")
    todo_lists = []
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if(todo_name != row[0]):
                todo_lists.append(row)
            else:
                todo_lists.append([0], "True")
        with open(file_name, "w") as f:
            writer = csv.writer(f)
            writer.writerows(todo_lists)

def view_todo(file_name):
    print("View todo")
    with open(file_name, "r") as f: # with statement, opens file & reads and closes
        reader = csv.reader(f) #reader variable = csv file reader
        reader.__next__() #This tells the reader to go to the next line
        for row in reader: # for loop to go through rows in the reader
            if (row[1] == "True"):
                print(f"Todo {row[0]} is completed")
            else:
                print(f"Todo {row[0]} is not complete")