import pytest
from selenium import webdriver

@pytest.fixture()
def setup(browser):
    if browser=='chrome':

        driver=webdriver.Chrome()
        print("Launching chrome browser.........")
    elif browser=='edge':
        driver = webdriver.Edge()
        print("Launching edge browser.........")
    return driver

def pytest_addoption(parser):    # This will get the value from CLI /hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")

def pytest_configure(config):
    config._metadata = {
        'Project Name': 'nop Commerce',
        'Module Name': 'Customers',
        'Tester': 'Pavan'
    }

@pytest.fixture()
def run_number(request):
    return request.param

# # Hook for delete/Modify Environment info to HTML Report
# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     if 'JAVA_HOME' in metadata:
#         del metadata['JAVA_HOME']
#     if 'Plugins' in metadata:
#         del metadata['Plugins']
########### pytest HTML Report ################

# # It is hook for Adding Environment info to HTML Report
# def pytest_configure(config):
#     config._metadata['Project Name'] = 'nop Commerce'
#     config._metadata['Module Name'] = 'Customers'
#     config._metadata['Tester'] = 'Pavan'
#
# # It is hook for delete/Modify Environment info to HTML Report
# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop("JAVA_HOME", None)
#     metadata.pop("Plugins", None)
# Hook for Adding Environment info to HTML Report



