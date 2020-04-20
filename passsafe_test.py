import unittest
from passsafe import User

class TestPassword(unittest.TestCase):

    '''
    test class that define taste cases for the password class
    '''

    def setUp(self):
        '''
        method to run before each test cases
        '''
        self.new_user = User("Kevin","Muneneee","instagram","password")

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
        self.assertEqual(self.new_user.username,"Muneneee")
        self.assertEqual(self.new_user.account,"instagram")
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
        test_user = User("Test","name","instagram","password")
        test_user.save_user()

        self.new_user.delete_user()
        self.assertEqual(len(User.user_list),1)


if __name__ == '__main__':
    unittest.main()
    