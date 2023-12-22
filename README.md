# T1A3 - Terminal Application Assignment - Ronald Kwan

## Name of application (OnePWD Manager)
![Alt text](/docs/SS1.JPG)
This is the home page where you can login, make a new user or find out more about ONEPWD.
![Alt text](/docs/SS2.JPG)
Once you have logged in, you can access a few features, including how to view some passwords, adding passwords, deleteing them or even looking at a report.
![Alt text](/docs/SS3.JPG)
If the system recognises there are no passwords, it will prompt the user to do so.
![Alt text](/docs/SS4.JPG)
Passwords can be added manually, the application will also look how secure the password is, by giving a password rating for security reasons
![Alt text](/docs/SS5gen.JPG)
Passwords can be generated by the application to give more security and ease for the user. A bonus feature, once the password has been generated and saved, it will copy to the clipboard for instant use!
![Alt text](/docs/SS6.JPG)
Passwords can be deleted, if user has put in correct details, that will be enabled and confirmed by the application.
![Alt text](/docs/SS7.JPG)
Reports is generated for user engagement, knowing when they logged in, and how many passwords is in the vault and how many generated.
![Alt text](/docs/SS8.JPG)
FAQ section is supplied for more information to the user, understanding why its created and how its useful for then.

## Link to source control repository
url: https://github.com/ronaldkwan93/-RonaldKwan-_T1A3

## Identify any code style guide or styling conventions
Coding Style: PEP 8

## Develop a list of features
### Feature (1) Create Login
### Feature (2) Login- Data Validation
### Feature (3) Store passwords
### Feature (4) View passwords
### Feature (5) Add passwords - Manually
### Feature (6) Add passwords - Generate password
### Feature (7) Rating password's strength
### Feature (8) Deleting passwords
### Feature (9) Password Report: Last Login
### Feature (10) Password Report: Password Count
### Feature (11) Password Report: Password Generated Count

## Implementation plan
### 1. How each feature will be implemented
1. Understand what each feature does & what it looks like
2. What does each feature need (requirements)
3. Build the feature (coding)
4. Test the feature (unit tests)
5. Implement new logic
6. Test the feature (reiterate testing)
7. Production
### 2. Checklist of tasks for each feature (at least 5)
### Feature (1) Create New Login
1. Create menu for user to select a new user
2. Create if statement (User chooses option 1)
3. Create new_user function  
4. Check new_user function requires input from user, opens cvs file, reads it and gives response of successful Login or Login already exist logic.
5. Test user input and expected output with function
### Feature (2) Login- Data Validation
1. Create inputs (user_name) & (user_pass)
2. Create opening file and reading existing user list
3. Create If statement within file reading to check user_name and user_pass is matched within the for loop
4. Create if the username isn't found, to print error
5. Test user input and expected output with function
### Feature (3) View passwords
1. Create file open to look into user_list cvs
2. Create for loop to print out any data avaliable
3. If no data seen, print (No existing passwords, press 2 to continue)
4. Create parameters to print out information seperated with ","
5. Test user input and expected output with function
### Feature (4) Add passwords - Manually
1. Create while True Loop, with menu
2. If & Elif options for the menu items
3. Create function password_list to create a cvs and print into it
4. In password_list function, create inputs (pwd_name & pwd_pwd) to print
5. With if condition, check length of password and output accordingly
6. Test user input and expected output with function
### Feature (5) Add passwords - Generate password
1. Create username to be stored
2. Generated password is to use random function and string function to form 12 character secure password
3. Create While True loop to ask user for confirmation
4. Within While Loop to have an iF statement to write generated password into another CVS file.
5. Create copy to clipboard function using pyperclip function
6. Test user input and expected output with function
### Feature (6) Store passwords
Similar steps to Feature 4 & 5 included
### Feature (7) Rating password's strength
Similar steps to Feature 4 included
### Feature (8) Deleting passwords
1. Create variables as empty figures
2. Create password_delete function, Create input to double check user intention
3. Create With statement to open file 
4. Create For statement within With to scan all passwords inside
5. Create IF statement within that For statement to print what is not been inputed if matched
6. Create if Not found match to create an error message
7. Test user input and expected output with function
### Feature (9) Password Report: Last Login, Password Count, Password Generated Count
1. Create variable that collects current time and date, using import Datetime
2. Create a line count variable
3. Create a count line function using a For loop to look at the cvs file
4. Create exceptions when file doesn't exists
5. Test user input and expected output with function


### 3. Priority: implementation of different features
1. Creating Login accounts
2. Login - Data Validation
3. Adding passwords
4. Storing passwords
5. Viewing passwords
6. Deleting passwords
7. Generating passwords
8. Password Report: Last Login
9. Password Report: Password Count
10. Password Report: Password Generated Report
11. Rating password strength


### 4. Deadline for each feature
#### 2 WEEK SPRINT (4 blocks, 3.5 days each)
#### 1st Block
1. Create Login
2. Login-Data Validation
3. View Passwords
#### 2nd Block
1. Store Passwords
2. Add Passwords- Manually
3. Deleting Passwords
#### 3rd Block
1. Add Passwords- Generate password
2. Rating password's strength
3. Password Report: Last Login
#### 4th Block
1. Password Report: Password Count
2. Password Report: Password Generated Count
### 5. Project management platform
Trello
### 6. Screenshots: Trello
![Alt text](/docs/image.png)
## Design help documentation
### 1. Instructions: How to use
Once run the program all prompts are expected by the user on the screen.
1. Expected inputs are numbers (1-5)
2. To confirm important decisions (Y/N)
### 2. Instructions: How to install the application
(PLEASE NOTE: Start by opening up your terminal of choice)
1. Lead your directory to where you want to install the application
"cd desktop"
2. Clone the Repo from Github: https://github.com/ronaldkwan93/RonaldKwan_T1A3
3. In terminal, run - ./run.sh
### 3. Instructions: Dependancies required for OnePWD Manager
1. Python
2. Terminal
3. Imports
- Colored
- csv
- os 
- random
- string
- pyperclip
- datetime
### 4. System/Hardware requirements for OnePWD Manager
#### System
1. Operating System:
Terminal applications are designed to run on various operating systems, including Linux, macOS, and Windows
#### Hardware
1. Most terminal-based programs can run on systems with minimal RAM and processor speed
### 5. Command line arguments for OnePWD Manger
(Optional, everything will be run through ./run.sh)\
1. Python3 main.py
2. Control + C to interupt program