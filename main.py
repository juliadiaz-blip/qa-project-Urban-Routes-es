from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import data
from data import FROM_STREET, TO_STREET, DATA_URL
from pages import UrbanRoutesPage


class TestUrbanRoutes:

    driver = None
    urbanroutespage = None

    @classmethod
    def setup_class(cls):
        options = Options()
        options.set_capability("goog:loggingPrefs", {"performance": "ALL"})

        service = Service(ChromeDriverManager().install())

        cls.driver = webdriver.Chrome(
            service=service,
            options=options
        )

        cls.driver.get(DATA_URL)

        cls.urbanroutespage = UrbanRoutesPage(cls.driver)

    def setup_method(self):
        self.driver.get(DATA_URL)

    def preparar_pedido(self):
        self.urbanroutespage.seleccionar_tarifa_comfort()
        self.urbanroutespage.click_phone_number()

    def test_set_route(self):
        self.urbanroutespage.set_route()

        assert self.urbanroutespage.get_from() == FROM_STREET
        assert self.urbanroutespage.get_to() == TO_STREET

    def test_verificar_tarifa_confort(self):
        self.urbanroutespage.set_route()
        self.urbanroutespage.click_button_reservar()
        self.urbanroutespage.click_tarifa_comfort()

        assert self.urbanroutespage.obtener_texto_tarifa_comfort() == "Comfort"

    def test_agregar_tarjeta(self):
        self.preparar_pedido()
        self.urbanroutespage.click_payment_method_button()
        self.urbanroutespage.click_add_card_button()
        self.urbanroutespage.set_card()

        assert self.urbanroutespage.get_phone_value() == data.PHONE_NUMBER

    def test_agregar_tarjeta(self):
        self.preparar_pedido()
        self.urbanroutespage.click_payment_method_button()
        self.urbanroutespage.click_add_card_button()
        self.urbanroutespage.set_card()

        assert self.urbanroutespage.get_payment_method_text() == "tarjeta"

    def test_mensaje_para_conductor(self):
        self.preparar_pedido()
        self.urbanroutespage.set_driver_message()

        assert self.urbanroutespage.get_driver_message_text() == data.MESSAGE_FOR_DRIVER

    def test_manta_y_panuelos(self):
        self.preparar_pedido()
        self.urbanroutespage.click_blanket_and_tissues()

        assert self.urbanroutespage.get_blanket_status()

    def test_pedir_dos_helados(self):
        self.preparar_pedido()
        self.urbanroutespage.add_ice_cream()

        assert self.urbanroutespage.get_ice_cream_count() == 2

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()