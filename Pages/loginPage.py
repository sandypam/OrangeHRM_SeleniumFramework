from Pages.BasePage import BasePage

class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)


    def login(self, username, password):
        self.type("username_NAME", username)
        self.type("password_NAME", password)
        self.click("loginButton_XPATH")
        return self.get_text("pageTitle_XPATH")


