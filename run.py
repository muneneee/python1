#!/usr/bin/env python3.6

from passsafe import User
import random

def create_user(name,username,account,password):
    new_user = User(name,username,account,password)
    return new_user


def save_users(user):
    user.save_user()


def del_user(user):
    user.delete_user()


def display_details():
    return User.display_details()