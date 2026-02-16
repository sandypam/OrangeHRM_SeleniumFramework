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
        header.text.strip().lower(): idx
        for idx, header in enumerate(headers)
        if header.text and header.text.strip()
    }

    col_key = column_name.strip().lower()

    if col_key not in header_map:
        available = ", ".join(header_map.keys())
        raise ValueError(
            f"Column '{column_name}' not found in table. Available columns: {available}"
        )

    column_index = header_map[col_key]

    rows = table_element.find_elements(*row_locator)
    for row in rows:
        cells = row.find_elements(*cell_locator)
        if column_index < len(cells):
            cell_text = cells[column_index].text.strip()
            if cell_text == expected_value.strip():
                return row

    return None