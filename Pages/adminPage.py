from Pages.BasePage import BasePage
from Utilities.table_utils import find_row_by_column_value

class AdminPage(BasePage):

    def _loc(self, key: str):
        return (self._by(key), self._locator_value(key))

    def find_user_row(self, username: str):
        table = self.wait_for_visible("admin_table_XPATH")

        return find_row_by_column_value(
            table,
            self._loc("admin_table_headers_XPATH"),
            self._loc("admin_table_rows_XPATH"),
            self._loc("admin_table_cells_XPATH"),
            "Username",
            username
        )
