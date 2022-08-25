import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options as FFO

#pytest -s -v --browser_name=<firefox or chrome> --language=<en/ru/es> file-name.py
def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='en-gb',
                     help="Choose language: ru/en/es ..")

@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        fp = FFO()
        fp.set_preference('intl.accept_languages', user_language)
        service = Service(r'C:\geckodriver\geckodriver.exe')
        browser = webdriver.Firefox(service=service, options=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()