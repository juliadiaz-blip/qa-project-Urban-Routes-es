from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import data
from helpers import retrieve_phone_code
from selenium.webdriver import Keys


class UrbanRoutesPage:
    FROM_FIELD = (By.ID, "from")
    TO_FIELD = (By.ID, "to")
    BUTTON_RESERVAR = (By.XPATH, "//button[@class='button round']")
    TARIFA_COMFORT = (By.XPATH, "//div[text()='Comfort' and @class='tcard-title']")
    PHONE_NUMBER_BUTTON = (By.XPATH,"//div[text()='Número de teléfono']")
    PHONE_INPUT = (By.ID, "phone")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Siguiente']")
    CODE_INPUT = (By.ID, "code")
    CONFIRM_BUTTON = (By.XPATH, "//button[text()='Confirmar']")
    CLOSE_PHONE_MODAL = (By.XPATH, "//div[@class='number-picker open']//button[contains(@class,'section-close')]")
    ADD_CARD_BUTTON = (By.XPATH, "//div[@class='pp-row disabled']//div[text()='Agregar tarjeta']")
    PAYMENT_METHOD_BUTTON = (By.CLASS_NAME, "pp-button")
    CARD_NUMBER_INPUT = (By.XPATH, "//input[@id='number' and @name='number']")
    CARD_CODE_INPUT = (By.XPATH, "//div[@class='card-code-input']//input[@id='code']")
    ADD_BUTTON = (By.XPATH, "//button[text()='Agregar']")
    DRIVER_MESSAGE_INPUT = (By.ID, "comment")
    BLANKET_AND_TISSUES_SWITCH = (By.CLASS_NAME, "switch-input")
    ICE_CREAM_PLUS = (By.CLASS_NAME, "counter-plus")
    ORDER_TAXI_BUTTON = (By.XPATH, "//button[contains(@class,'smart-button')]")
    SEARCH_CAR_MODAL = (By.XPATH, "//div[text()='Buscar automóvil']")
    DRIVER_INFO_MODAL = (By.XPATH, "//div[contains(text(),'El conductor llegará')]")
    PAYMENT_METHOD_DISPLAY = (By.CLASS_NAME,"pp-value-text")
    ICE_CREAM_COUNTER = (By.CLASS_NAME,"counter-value")

    def __init__(self, driver):
        self.driver = driver

    def set_from_field(self):
        from_field = WebDriverWait(
            self.driver,
            20
        ).until(
            expected_conditions.visibility_of_element_located(
                self.FROM_FIELD
            )
        )

        from_field.clear()
        from_field.send_keys(data.FROM_STREET)

    def set_to_field(self):
        to_field = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(self.TO_FIELD)
        )
        to_field.clear()
        to_field.send_keys(data.TO_STREET)

    def set_route(self):
        self.set_from_field()
        self.set_to_field()

    def get_from(self):
        return self.driver.find_element(
            *self.FROM_FIELD
        ).get_property("value")

    def get_to(self):
        return self.driver.find_element(
            *self.TO_FIELD
        ).get_property("value")

    def click_button_reservar(self):
        button_reservar = WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(self.BUTTON_RESERVAR))
        button_reservar.click()

    def obtener_texto_tarifa_comfort(self):
        tarifa_comfort = self.driver.find_element(*self.TARIFA_COMFORT)
        return tarifa_comfort.text

    def seleccionar_tarifa_comfort(self):
        self.set_route()
        self.click_button_reservar()
        self.click_tarifa_comfort()

    def click_tarifa_comfort(self):
        tarifa_comfort = WebDriverWait(
            self.driver,
            timeout=10
        ).until(
            expected_conditions.element_to_be_clickable(
                self.TARIFA_COMFORT
            )
        )

        tarifa_comfort.click()

    def click_phone_number(self):

        phone_number_button = WebDriverWait(
            self.driver,
            20
        ).until(
            expected_conditions.element_to_be_clickable(
                self.PHONE_NUMBER_BUTTON
            )
        )

        phone_number_button.click()

    def set_phone_number(self):
        phone_input = WebDriverWait(
            self.driver,
            10
        ).until(
            expected_conditions.visibility_of_element_located(
                self.PHONE_INPUT
            )
        )

        phone_input.clear()
        phone_input.send_keys(data.PHONE_NUMBER)

    def click_next_button(self):
        next_button = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(self.NEXT_BUTTON))
        next_button.click()

    def set_code(self, code):
        code_input = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(
                self.CODE_INPUT
            )
        )
        code_input.clear()
        code_input.send_keys(code)

    def click_confirm_button(self):
        confirm_button = WebDriverWait(
            self.driver,
            10
        ).until(
            expected_conditions.element_to_be_clickable(
                self.CONFIRM_BUTTON
            )
        )

        confirm_button.click()

    def close_phone_modal(self):
        close_button = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(
                self.CLOSE_PHONE_MODAL
            )
        )
        self.driver.execute_script("arguments[0].click();", close_button)

    def click_payment_method_button(self):
        payment_button = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(
                self.PAYMENT_METHOD_BUTTON
            )
        )
        self.driver.execute_script("arguments[0].click();", payment_button)

    def get_phone_code(self):
        code = retrieve_phone_code(self.driver)

        return code

    def click_add_card_button(self):
        add_card_button = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(
                self.ADD_CARD_BUTTON
            )
        )
        self.driver.execute_script("arguments[0].click();", add_card_button)

    def set_card_number(self):
        card_number_input = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(
                self.CARD_NUMBER_INPUT
            )
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", card_number_input)
        self.driver.execute_script("arguments[0].click();", card_number_input)
        card_number_input.send_keys(data.CARD_NUMBER)

    def set_card_code(self):
        card_code_input = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(
                self.CARD_CODE_INPUT
            )
        )
        card_code_input.send_keys(data.CARD_CODE)
        card_code_input.send_keys(Keys.TAB)


    def click_add_button(self):
        add_button = WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(self.ADD_BUTTON))
        add_button.click()

    def set_card(self):
        self.set_card_number()
        self.set_card_code()
        self.click_add_button()

    def set_driver_message(self):
        driver_message_input = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(self.DRIVER_MESSAGE_INPUT))

        driver_message_input.clear()
        driver_message_input.send_keys(data.MESSAGE_FOR_DRIVER)

    def click_blanket_and_tissues(self):
        switch = WebDriverWait(
            self.driver,
            10
        ).until(
            expected_conditions.presence_of_element_located(
                self.BLANKET_AND_TISSUES_SWITCH
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);",
            switch
        )

        self.driver.execute_script(
            "arguments[0].click();",
            switch
        )

    def add_ice_cream(self):
        ice_cream_plus = WebDriverWait(
            self.driver,
            10
        ).until(
            expected_conditions.element_to_be_clickable(
                self.ICE_CREAM_PLUS
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);",
            ice_cream_plus
        )

        self.driver.execute_script(
            "arguments[0].click();",
            ice_cream_plus
        )

        self.driver.execute_script(
            "arguments[0].click();",
            ice_cream_plus
        )

    def click_order_taxi_button(self):
        order_taxi_button = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(self.ORDER_TAXI_BUTTON))
        order_taxi_button.click()

    def get_search_car_modal_text(self):
        search_car_modal = WebDriverWait(self.driver, 30).until(
            expected_conditions.visibility_of_element_located(self.SEARCH_CAR_MODAL))
        return search_car_modal.text

    def get_driver_info_text(self):
        driver_info = WebDriverWait(self.driver, 60).until(
            expected_conditions.visibility_of_element_located(self.DRIVER_INFO_MODAL))
        return driver_info.text

    def get_phone_value(self):
        return self.driver.find_element(
            *self.PHONE_INPUT
        ).get_attribute("value")

    def get_payment_method_text(self):
        return self.driver.find_element(*self.PAYMENT_METHOD_DISPLAY).text

    def get_driver_message_text(self):
        return self.driver.find_element(*self.DRIVER_MESSAGE_INPUT).get_property("value")

    def get_blanket_status(self):
        return self.driver.find_element(*self.BLANKET_AND_TISSUES_SWITCH).is_selected()

    def get_ice_cream_count(self):
        return int(self.driver.find_element(*self.ICE_CREAM_COUNTER).text)