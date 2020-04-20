class User:
    '''
    class that generates new instances of users
    '''
    
    user_list = []


    def __init__(self,name,password):

        self.name = name
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


    @classmethod
    def find_by_number(cls,number):
        '''
        takes name and return user matching
        '''
        for user in cls.user_list:
            if user.password == number:
                return user




class Credentials:
    '''
    class for creating new instances of accounts
    '''


    account_list = []


    def __init__(self,username,account,accountpassword):

        self.username = username
        self.account = account
        self.accountpassword = accountpassword

    def save_account(self):
        '''
        a method for saving the account
        '''
        Credentials.account_list.append(self)


    def delete_account(self):
        '''
        method for deleting accounts
        '''
        Credentials.account_list.remove(self)


    @classmethod
    def display_accounts(cls):
        '''
        method to display user accounts
        '''
        return cls.account_list
