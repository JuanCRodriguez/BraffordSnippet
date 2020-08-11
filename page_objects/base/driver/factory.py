import json
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import requests


class LocalDriverFactory:

    def __init__(self, browser):  # todo: implementar firefox en un futuro
        self.browser = browser

    def build_driver(self, o: Options):
        return webdriver.Chrome(desired_capabilities=o.to_capabilities(),
                                executable_path=ChromeDriverManager(log_level=0).install())


class RemoteDriverFactory:

    def __init__(self, command_executor):
        self._command_executor = command_executor

    def _wait_for_slot(self):
        tries = 0
        while tries <= 3:
            response = requests.get(f"{self._command_executor}/status")
            try:
                estado = response.json()['value']['ready']
            except:
                estado = None
            if not estado:
                sleep(10)
                tries += 1
            else:
                return estado
        raise Exception("El hub no estaba disponible")

    def build_driver(self, o: Options):
        self._wait_for_slot()
        return webdriver.Remote(command_executor=self._command_executor,
                                desired_capabilities=o.to_capabilities())
