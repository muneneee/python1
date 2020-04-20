import unittest
from passsafe import User
from passsafe import Credentials

class TestPassword(unittest.TestCase):

    '''
    test class that define taste cases for the password class
    '''

    def setUp(self):
        '''
        method to run before each test cases
        '''
        self.new_user = User("Kevin","password")

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.user_list = []

    def test_init(self):
        '''
        test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.name,"Kevin")
        self.assertEqual(self.new_user.password,"password")


    def test_save_user(self):
        '''
        testing the save_user method
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)


    def test_display_details(self):
        '''
        tests for display_details method
        '''
        self.assertEqual(User.display_details(),User.user_list)



    def test_delete_user(self):
        '''
        test for deleting users
        '''
        self.new_user.save_user()
        test_user = User("Test","name")
        test_user.save_user()

        self.new_user.delete_user()
        self.assertEqual(len(User.user_list),1)


    def test_save_multiple_users(self):
        '''
        to check if we can save multiple users
        '''
        self.new_user.save_user()
        test_user = User("Test","name")
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)


class TestAccount(unittest.TestCase):


    def setUp(self):

        self.new_account = Credentials("muneneee","instagram","password")

    
    def tearDown(self):
        Credentials.account_list = []

    
    def test_init(self):

        self.assertEqual(self.new_account.username,"muneneee")
        self.assertEqual(self.new_account.account,"instagram")
        self.assertEqual(self.new_account.accountpassword,"password")

    
    def test_save_account(self):


        self.new_account.save_account()
        self.assertEqual(len(Credentials.account_list),1)


    def test_display_accounts(self):

        self.assertEqual(Credentials.display_accounts(),Credentials.account_list)

    
    def test_delete_account(self):
        self.new_account.save_account()

        test_account = Credentials("Test","username","account")
        test_account.save_account()

        self.new_account.delete_account()
        self.assertEqual(len(Credentials.account_list),1)


    def test_save_multiple_accounts(self):
        self.new_account.save_account()
        test_account = Credentials("Test","username","account")
        test_account.save_account()
        self.assertEqual(len(Credentials.account_list),2)


if __name__ == '__main__':
    unittest.main()
    