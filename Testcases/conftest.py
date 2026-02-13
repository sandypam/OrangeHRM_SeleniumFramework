import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from Pages.loginPage import LoginPage
from Utilities.credentials import get_credentials
from Utilities import configReader
from dotenv import load_dotenv
load_dotenv()

# Setup Chrome options
chrome_options = Options()
chrome_options.add_argument("--start-maximized")  # open browser maximized
chrome_options.add_argument("--disable-notifications")  # disable notifications
# chrome_options.add_experimental_option("detach", True) # Keeps window open

@pytest.fixture(params=["chrome", "firefox"], scope="class")
def get_browser(request):
    if request.param == "chrome":
        driver = webdriver.Chrome(options=chrome_options)
    elif request.param == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported browser type: {request.param}")

    request.cls.driver = driver
    driver.get(configReader.readConfig("basic info", "testsiteurl"))
    yield driver
    driver.quit()

def _get_creds():
    # Pulls user and password from get_credentials
    user, pwd = get_credentials()
    if not user or not pwd:
        raise ValueError("Missing ORANGEHRM_USERNAME / ORANGEHRM_PASSWORD in env/.env")
    return user, pwd

@pytest.fixture(scope="class")
def logged_in(get_browser, request):
    username, password = get_credentials()
    LoginPage(get_browser).login(username, password)
    return get_browser

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep) # creates item.rep_setup / rep_call / rep_teardown

@pytest.fixture()
def log_on_failure(request, get_browser):
    yield
    item = request.node
    driver = get_browser
    rep_call = getattr(item, "rep_call", None)
    rep_setup = getattr(item, "rep_setup", None)

    # Attach screenshot if setup failed OR test call failed
    failed = (rep_setup and rep_setup.failed) or (rep_call and rep_call.failed)
    if failed:
        allure.attach(
            driver.get_screenshot_as_png(),
            name=item.name,
            attachment_type=AttachmentType.PNG
        )


