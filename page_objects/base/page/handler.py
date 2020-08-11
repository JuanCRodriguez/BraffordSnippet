from typing import List, Dict

from page_objects.base.page.base_page import BasePage, Locator


class PageHandler:
    url: str
    _initial_validations: Dict[Locator, str] = {}
    _initial_elements: List[Locator] = []

    def __init__(self, driver):
        self._bp = BasePage(driver)
        self._bp.wait_for_url(self.url)
        self._validate()

    def _validate(self):
        for locator in self._initial_elements:
            self._bp.find_element(locator)

        for locator, mensaje in self._initial_validations.items():
            self._bp.element_text_equals(locator, mensaje)



