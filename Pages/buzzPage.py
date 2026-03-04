from Pages.BasePage import BasePage


class BuzzPage(BasePage):

    def open_buzz(self):
        self.click("buzzLink_XPATH")
