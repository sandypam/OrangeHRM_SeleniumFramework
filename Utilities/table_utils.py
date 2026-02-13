# Utilities/table_utils.py
from typing import Optional
from selenium.webdriver.remote.webelement import WebElement

def find_row_by_column_value(
    table_element: WebElement,
    header_locator: tuple,
    row_locator: tuple,
    cell_locator: tuple,
    column_name: str,
    expected_value: str
) -> Optional[WebElement]:

    headers = table_element.find_elements(*header_locator)
    header_map = {
        header.text.strip(): idx
        for idx, header in enumerate(headers)
    }

    if column_name.lower() not in header_map:
        raise ValueError(f"Column '{column_name}' not found in table")

    column_index = header_map[column_name]

    rows = table_element.find_elements(*row_locator)
    for row in rows:
        cells = row.find_elements(*cell_locator)

        if column_index < len(cells) and cells[column_index].text.strip() == expected_value:
            return row

    return None
