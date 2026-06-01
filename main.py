import data

from selenium import webdriver

from pages import UrbanRoutesPage


class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):

        from selenium.webdriver.chrome.options import Options

        options = Options()

        options.set_capability(
            "goog:loggingPrefs",
            {"performance": "ALL"}
        )

        cls.driver = webdriver.Chrome(
            options=options
        )

        def test_set_route(self):
            self.driver.get(data.urban_routes_url)
            routes_page = UrbanRoutesPage(self.driver)
            address_from = data.address_from
            address_to = data.address_to
            routes_page.set_route(address_from, address_to)
            assert routes_page.get_from() == address_from
            assert routes_page.get_to() == address_to



    def test_call_taxi(self):

        self.driver.get(data.urban_routes_url)

        routes_page = UrbanRoutesPage(self.driver)

        routes_page.wait_for_load_home_page()

        routes_page.set_route(
            data.address_from,
            data.address_to
        )

        routes_page.click_call_taxi_button()

    def test_select_comfort_rate(self):

        self.driver.get(data.urban_routes_url)

        routes_page = UrbanRoutesPage(self.driver)

        routes_page.wait_for_load_home_page()

        routes_page.set_route(
            data.address_from,
            data.address_to
        )

        routes_page.click_call_taxi_button()

        routes_page.click_comfort_rate()

    @classmethod
    def teardown_class(cls):

        cls.driver.quit()