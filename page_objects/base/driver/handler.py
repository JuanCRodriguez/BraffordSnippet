from selenium.webdriver.chrome.options import Options


def get_options(headless):
    options = Options()
    options.headless = headless
    options.add_argument('--window-size=1920,1080')
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--lang=es_AR")
    options.set_capability('goog:loggingPrefs', {'browser': 'ALL'})
    options.set_capability('version', "83.0.4103.39")
    return options

class DriverHandler:

    def __init__(self, ambiente, factory, headless=False):
        self._factory = factory
        self.ambiente = ambiente
        self._main_driver = None
        self._drivers = []
        self._active_driver = None
        self._options = get_options(headless)

    def build_main_driver(self):
        if self._main_driver is not None:
            raise Exception("Ya existia un driver principal")
        self._main_driver = self.new_driver()
        return self.main_driver

    def new_driver(self):
        driver = self._factory.build_driver(self._options)
        driver.maximize_window()
        driver.get(self.ambiente)
        self._active_driver = driver
        self._drivers.append(driver)
        return driver

    @property
    def active_driver(self):
        return self._active_driver

    @property
    def drivers(self):
        return self._drivers

    @property
    def main_driver(self):
        return self._main_driver

    def close(self, driver):
        next(driver_ for driver_ in self._drivers if driver_ == driver).quit()

    def quit(self):
        for driver in self._drivers:
            try:
                driver.quit()
            except Exception as e:
                print("pincho", e)

    def __iter__(self):
        return iter(self.drivers)