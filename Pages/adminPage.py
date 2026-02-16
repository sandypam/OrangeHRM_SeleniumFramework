from Pages.BasePage import BasePage
from Utilities.table_utils import find_row_by_column_value

class AdminPage(BasePage):

    def open(self):
        self.click("adminLink_XPATH")

        # Wait for a admin element on admin page
        self.wait_for_visible("admin_search_userName_XPATH", timeout=15)

        return self

    def search_user(self, username: str):
        self.type("admin_search_userName_XPATH", username)
        self.click("admin_submit_Button_XPATH")

        # Wait for results table to be visible / stable
        self.wait_for_visible("admin_table_XPATH", timeout=15)

    def _loc(self, key: str):
        return (self._by(key), self._locator_value(key))

    def find_user_row(self, username: str):
        table = self.wait_for_visible("admin_table_XPATH", timeout=15)
        return find_row_by_column_value(
            table,
            self._loc("admin_table_headers_XPATH"),
            self._loc("admin_table_rows_XPATH"),
            self._loc("admin_table_cells_XPATH"),
            "Username",
            username
        )
