import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()  # ("/usr/bin/chromedriver")
        print("Launching Chrome browser........")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Launching Firefox browser........")
    else:
        driver = webdriver.Chrome()  # ("/usr/bin/chromedriver")
    return driver

def pytest_addoption(parser):                           # this will get the value from CLI / hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):                                   # this will return the browser value to setup method
    return request.config.getoption("--browser")

#######################pytest html report ###########################
# it hooks for adding environment info to html report
def pytest_configure (config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'customer'
    config._metadata['Tester'] = 'khemlall'

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugin", None)