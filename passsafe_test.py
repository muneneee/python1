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

    