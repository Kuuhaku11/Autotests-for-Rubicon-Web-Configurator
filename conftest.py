import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as OptionsFirefox
from loguru import logger
import sys


#  Все логи записываются в "test_log.log", но начало и окончание тестов не отображаются в терминале
logger.remove()
logger.add('logs/test_log.log', format='{time:MMMM D, YYYY > HH:mm:ss} | {level} | {message}',
           level='DEBUG', rotation='200 KB')
logger.add(sys.stderr, level='INFO')

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help='Choose browser: chrome или firefox')


@pytest.hookimpl(tryfirst=True)
def pytest_sessionstart():  # Выполняется перед началом всех тестов
    logger.debug("=== НАЧАЛО ТЕСТОВ ===")


@pytest.hookimpl(tryfirst=True)
def pytest_sessionfinish():  # Выполняется после окончания всех тестов
    logger.debug("=== ЗАВЕРШЕНИЕ ТЕСТОВ ===\n\n\n")


def pytest_runtest_makereport(call):
    """Хук, который вызывается после выполнения каждого теста.
    Используется для обработки результатов тестов и логгирования assert ошибок.
    """
    if call.when == 'call':  # Проверяет выполнен ли тест
        if call.excinfo is not None:  # Проверяет есть ли информация в ошибке
            logger.error(call.excinfo.value)
        logger.info('Quit browser...\n')


@pytest.fixture(scope='function')
def browser(request, headless):
    browser_name = request.config.getoption('browser_name')
    if browser_name == 'chrome':
        print()
        logger.info(f'Start chrome for "{request.node.name}"...')
        options = Options()
        if headless:  # Если в настройках задан "True", то отображения в браузере не будет
            options.add_argument('headless=new')
        options.add_experimental_option('excludeSwitches', ['enable-logging'])  # Подавление DevTools
        browser = webdriver.Chrome(options=options)
    elif browser_name == 'firefox':
        print()
        logger.info('\nStart firefox for test...')
        options = OptionsFirefox()
        if headless:
            options.add_argument('--headless')
        browser = webdriver.Firefox(options=options)
    else:
        raise pytest.UsageError('--browser_name should be chrome or firefox')
    yield browser
    browser.quit()