#!/usr/bin/env python3.6

from passsafe import User
from passsafe import Credentials
import random

def create_user(name,password):
    new_user = User(name,password)
    return new_user


def save_user(user):
    user.save_user()


def del_user(user):
    user.delete_user()


def display_details():
    return User.display_details()


def find_user(number):
    return User.find_by_number(number)

def main():
    
    while True:
        print("HI welcome to passsafe.If you want to sign up enter :(s) if to log in enter :(l)")
        action = input()

    
        if action == "s":
            print ("New user")
            print ("-"*10)
            print("Enter your name")
            name = input()

            print("Set your password")
            password = input()

            save_user(create_user(name,password))
            print('\n')
            print(f"New user {name} created")
            print("You can log in with the details")
            print('\n')

        elif action == "l":
            print("Enter your name")
            loginname = input()

            print("Enter password...")
            loginpassword = input()

            if find_user(loginpassword):
                print('\n')
                print("To add account, press: a")
                print("-"*10)
                print("To view accounts, press: v")

                choice = input()
                print('\n')

                if choice == "a":
                    print("Add account")
                    print("-"*10)
                    print("Enter account name")
                    account = input()
                    print('\n')
                    print("Enter account username")
                    username = input()
                    print('\n')
                    
                    print("To generate password enter: g")
                    print("-"*10)
                    print("To input own password enter: p")
                    pick = input()
                    print('\n')


                    if pick == "g":
                        accountpassword = random.randint(10000,100000)
                        print(f"Password: {accountpassword}")





if __name__ == '__main__':

    main()

        


