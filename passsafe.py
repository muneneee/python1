class User:
    '''
    class that generates new instances of passwords
    '''
    
    user_list = []


    def __init__(self,name,username,account,password):

        self.name = name
        self.username = username
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
    accounts = []


    def __init__(self,username,account,accountpassword):

        self.username = username
        self.account = account
        self.accountpassword = password

    def save_account(self):
        '''
        a method for saving the account
        '''
        Credentials.accounts.append(self)


    def delete_account(self):
        '''
        method for deleting accounts
        '''
        Credentials.accounts.remove(self)


    @classmethod
    def display_account(cls):
        '''
        method to display user accounts
        '''
        return cls.accounts
