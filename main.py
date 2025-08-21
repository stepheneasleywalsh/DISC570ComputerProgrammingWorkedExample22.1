import sys

username = input("Username: ")
password = input("Password: ")

if username=="admin" and password=="Password123!":
    print("Correct")
else:
    print("YOU SHALL NOT PASS HACKER.... ending program early")
    sys.exit() # Stop running Python

print("ok, what would you like to do?")
# Actions can go here