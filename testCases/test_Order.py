import unittest
from testCases.test_companySignUp import TestSignUp
from testCases.test_login import TestLogin

# get all tests from SearchText and HomePageTest class
companySignUp_test = unittest.TestLoader().loadTestsFromTestCase(TestSignUp)
Test_Login = unittest.TestLoader().loadTestsFromTestCase(TestLogin)

# create a test suite combining search_text and home_page_test
test_suite = unittest.TestSuite([companySignUp_test, Test_Login])


# run the suite
if __name__ == '__main__':
    if not hasattr(unittest, 'test_run'):
        unittest.test_run = True
        unittest.TextTestRunner(verbosity=2).run(test_suite)
