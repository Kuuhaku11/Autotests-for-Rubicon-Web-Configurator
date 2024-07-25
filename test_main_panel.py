from test_cases.main_panel import MainPanel
import pytest # type: ignore
import time


link = 'http://localhost:8082/'
version = '1.0.0.265'  # Необходимо указать актуальную версию конифгуратора для првоерки соотвествия.

def test_check_tab(browser):  # Проверка title
    page = MainPanel(browser, link)
    page.open()
    page.check_tab_name_on_title()  # Название вкладки
    page.check_version_on_title(version)  # Версия конфигуратора в title

@pytest.mark.test
def test_logo(browser):  # Проверка логотипа "Рубикон"
    page = MainPanel(browser, link)
    page.open()
    page.should_be_logo()  # Есть ли лого?
    page.does_page_refresh_when_click_logo()  # Обновляется ли страница при клике на лого?