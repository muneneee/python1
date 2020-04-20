class User:
    '''
    class that generates new instances of passwords
    '''
    
    user_list = []


    def __init__(self,name,username,account,password):

        self.name = name
        self.username = username
        self.account = account
        self.password = password

    def save_user(self):
        '''
        a method for saving the user
        '''
        User.user_list.append(self)


    def delete_user(self):
        '''
        method for deleting users
        '''
        User.user_list.remove(self)


    @classmethod
    def display_details(cls):
        '''
        method to display user details
        '''
        return cls.user_list


class Credentials:
    user_list = []


    def __init__(self,name,username,account,password):

        self.name = name
        self.username = username
        self.account = account
        self.password = password

    def save_user(self):
        '''
        a method for saving the user
        '''
        User.user_list.append(self)


    def delete_user(self):
        '''
        method for deleting users
        '''
        User.user_list.remove(self)


    @classmethod
    def display_details(cls):
        '''
        method to display user details
        '''
        return cls.user_list
