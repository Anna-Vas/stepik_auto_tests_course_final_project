import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as OptionsChrome
from selenium.webdriver.firefox.options import Options as OptionsFirefox

languages = ["ar", "ca", "cs", "da", "de", "en-gb", "el", "es", "fi",
             "fr", "it", "ko", "nl", "pl", "pt", "pt-br", "ro", "ru",
             "sk", "uk", "zh-cn", "en"]

def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default="en",
                       help="Choose a language")

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser")
    language = request.config.getoption("language")
    if language is not None and language in languages:
        browser = None
        if browser_name == "chrome":
            options_chrome = OptionsChrome()
            options_chrome.add_experimental_option(
                'prefs', {'intl.accept_languages': language})
            print("\nstart chrome browser for test...")
            browser = webdriver.Chrome(options=options_chrome)
        elif browser_name == "firefox":
            options_firefox = OptionsFirefox()
            options_firefox.set_preference("intl.accept_languages", language)
            print("\nstart firefox browser for test...")
            browser = webdriver.Firefox(options=options_firefox)
        else:
            raise pytest.UsageError("--browser should be chrome or firefox")
    else:
        raise pytest.UsageError("--language should be one of the possible languages")
    yield browser
    print("\nquit browser...")
    browser.quit()