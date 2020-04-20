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