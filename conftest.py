import pytest
from pygments.styles.dracula import yellow


@pytest.fixture(autouse=True)
def test_setup(browser):
    if browser=='Firefox':
        print("webdriver initialized with Firefox")
    elif browser=='Chrome':
        print("webdriver initialized with chrome")
    elif browser=='Safari':
        print("webdriver initialized with safari")
    elif browser=='Opera':
        print("webdriver initialized with opera")
    yield
    print("teardown successfully")

#to recognize --browser from cli to pytest
def pytest_addoption(parser): #hook
    parser.addoption("--browser")
@pytest.fixture
def browser(request):
     return request.config.getoption("--browser")