import unittest
from testCases.test_companySignUp import TestSignUp
from testCases.test_login import TestLogin
from testCases.test_configuration import TestConfiguration
from testCases.test_AddEmployees import addEmployees
from testCases.test_EmployeeSignUp import TestEmployeeSignUp
from testCases.test_networks import TestNetworks
from SunithaTestCase.test_profilePage import TestMyProfile
from SunithaTestCase.test_CompanyProfile import TestCompanyProfile
# from krishnatestCases.test_newsfeed import TestNewsFeed
# from testCases.test_MediaDrive import TestMediaDrive


# get all tests from SearchText and HomePageTest class
companySignUp_test = unittest.TestLoader().loadTestsFromTestCase(TestSignUp)
Test_Login = unittest.TestLoader().loadTestsFromTestCase(TestLogin)
Test_Conf = unittest.TestLoader().loadTestsFromTestCase(TestConfiguration)
Test_addEmp = unittest.TestLoader().loadTestsFromTestCase(addEmployees)
Test_EmpSignUp = unittest.TestLoader().loadTestsFromTestCase(TestEmployeeSignUp)
Test_Networks = unittest.TestLoader().loadTestsFromTestCase(TestNetworks)
Test_MyProfile = unittest.TestLoader().loadTestsFromTestCase(TestMyProfile)
Test_CompanyProfile = unittest.TestLoader().loadTestsFromTestCase(TestCompanyProfile)
# Test_NewsFeed = unittest.TestLoader().loadTestsFromTestCase(TestNewsFeed)
# Test_MediaDrive = unittest.TestLoader().loadTestsFromTestCase(TestMediaDrive)

# create a test suite combining search_text and home_page_test
test_suite = unittest.TestSuite([companySignUp_test, Test_Login,Test_Conf, Test_addEmp, Test_EmpSignUp, Test_Networks, Test_MyProfile, Test_CompanyProfile])
# test_suite = unittest.TestSuite([companySignUp_test, Test_Login, Test_Conf])



# run the suite
if __name__ == '__main__':
    if not hasattr(unittest, 'test_run'):
        unittest.test_run = True
        unittest.TextTestRunner(verbosity=2).run(test_suite)
