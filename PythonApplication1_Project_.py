import random
import string
while True:
    password_lengs = int(input("Enter the password length: ")) 
    if password_lengs <= 0:
       print("Password length must be greater than 0")
       continue
    elif password_lengs > 100:
       print("Password length must be less than 100")
       continue
    elif password_lengs > 0 and password_lengs <= 100:
       break
while True:
    Use_special_chars = input("Do you want to use special characters? (y/n): ")
    if Use_special_chars == "y":
       Use_special_chars = True
       break
    elif Use_special_chars == "n":
       Use_special_chars = False
       break
    else:
       print("Please enter y or n")
       continue
while True:
    Use_numbers = input("Do you want to use numbers? (y/n): ")
    if Use_numbers == "y":
       Use_numbers = True
       break
    elif Use_numbers == "n":
       Use_numbers = False
       break
    else:
       print("Please enter y or n")
       continue
while True:
    Use_uppercase = input("Do you want to use uppercase letters? (y/n): ")
    if Use_uppercase == "y":
       Use_uppercase = True
       break
    elif Use_uppercase == "n":
       Use_uppercase = False
       break
    else:
       print("Please enter y or n")
       continue
while True:
    Use_lowercase = input("Do you want to use lowercase letters? (y/n): ")
    if Use_lowercase == "y":
       Use_lowercase = True
       break
    elif Use_lowercase == "n":
       Use_lowercase = False
       break
    else:
       print("Please enter y or n")
       continue





