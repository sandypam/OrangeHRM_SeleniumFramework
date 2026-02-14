from Pages.BasePage import BasePage
from Utilities import configReader


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)


    def login(self, username, password):
        self.type("username_NAME", username)
        self.type("password_NAME", password)
        self.click("loginButton_XPATH")

    def logout(self):
        self.click("userMenu_XPATH")
        self.click("logout_XPATH")

    def open(self):
        self.driver.get(configReader.readConfig("basic info", "testsiteurl"))

    def title(self):
        return self.get_text("pageTitle_XPATH")

    def get_error_message(self):
        return self.get_text("invalidLoginMessage_XPATH")


