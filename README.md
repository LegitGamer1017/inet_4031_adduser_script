## Description Section

`create-users.py` is a Python script to automate the process of adding multiple users and groups to a Linux system. The script reads input from a file `create-users.input` that contains a list of users to add, creating user accounts, setting passwords, and assigning users to specified groups based on the input data.

## Operation Section  

- The script is only compatible with Python 2.
- The input file (`create-users.input`) must be correctly formatted with one user per line, each consisting of five fields separated by colons: username, password, last name, first name, and group list.
- Admin privileges ( sudo ) are required for user creation and group assignment.
# How to Run
- Edit the create-users.input file to include the users you want to add. Make sure you follow the 5 field format.
- Execute the script with admin privileges
- sudo ./create-users.py < create-users.input
OR 
- cat create-users.input | sudo ./create-users.py
- The script will prompt you for information like passwords for the newly created users.
