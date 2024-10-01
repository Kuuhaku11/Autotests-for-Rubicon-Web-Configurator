from main_page import get_memory_info_static
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as OptionsFirefox
from loguru import logger
import sys
import os
import time


#  Все логи записываются в "test_log.log", но начало и окончание тестов не отображаются в терминале
logger.remove()
logger.add('logs/test_log.log', format='{time:MMMM D, YYYY > HH:mm:ss} | {level} | {message}',
           level='DEBUG', rotation='100 KB')
logger.add(sys.stderr, level='INFO')

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help='Choose browser: chrome или firefox')


@pytest.hookimpl(tryfirst=True)
def pytest_sessionstart(session):  # Выполняется перед началом всех тестов
    for filename in os.listdir('screenshots'):  # Удаляет скрины падений прошлых тестов
        if filename != '.gitkeep':
            os.remove(f'screenshots/{filename}')
    session.start_time = time.time()
    logger.debug('=== НАЧАЛО ТЕСТОВ ===')


@pytest.hookimpl(tryfirst=True)
def pytest_sessionfinish(session):  # Выполняется после окончания всех тестов
    time_sec = int(time.time() - session.start_time)
    time_result = f'{time_sec // 3600}:{time_sec % 3600 // 60}:{time_sec % 60}'
    logger.debug(f'=== ЗАВЕРШЕНИЕ ТЕСТОВ ({time_result}) ===\n\n\n')


@pytest.hookimpl()
def pytest_runtest_makereport(call, item):  # Хук, который вызывается после выполнения каждого теста.
    if call.when == 'call':  # Проверяет выполнен ли тест
        if call.excinfo is not None:  # Проверяет есть ли информация в ошибке
            browser = item.funcargs.get('browser')
            browser.save_screenshot(f'screenshots/{time.strftime('%H-%M-%S_%d.%m.%Y')}_{item.name[:-7]}.png')
            logger.error(call.excinfo.value)
            get_memory_info_static(str(type(browser)).split('.')[2])
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
        # options.add_argument("--enable-precise-memory-info")  # TODO
        browser = webdriver.Chrome(options=options)
    elif browser_name == 'firefox':
        print()
        logger.info(f'Start firefox for "{request.node.name}"...')
        options = OptionsFirefox()
        if headless:
            options.add_argument('--headless')
        browser = webdriver.Firefox(options=options)
    else:
        raise pytest.UsageError('--browser_name should be chrome or firefox')
    yield browser
    browser.quit()