import pytest # type: ignore
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as OptionsFirefox


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help='Choose browser: chrome или firefox')


@pytest.fixture(scope='function')
def browser(request, browser_name):
    if browser_name == 0:
        browser_name = request.config.getoption('browser_name')
    if browser_name == 'chrome':
        print('\nStart chrome for test...')
        options = Options()
        options.add_argument('headless=new')
        browser = webdriver.Chrome(options=options)
    elif browser_name == 'firefox':
        print('\nStart firefox for test...')
        options = OptionsFirefox()
        options.add_argument('--headless')
        browser = webdriver.Firefox(options=options)
    else:
        raise pytest.UsageError('--browser_name should be chrome or firefox')
    yield browser
    print('\nQuit browser...')
    browser.quit()