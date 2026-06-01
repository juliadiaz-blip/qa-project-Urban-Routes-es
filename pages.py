from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class UrbanRoutesPage:

    # LOCATORS

    from_field = (
        By.ID,
        'from'
    )

    to_field = (
        By.ID,
        'to'
    )

    call_taxi_button = (
        By.CSS_SELECTOR,
        '.button.round'
    )

    comfort_rate = (
        By.XPATH,
        "//div[text()='Comfort']"
    )
    phone_field = (
        By.ID,
        'phone'
    )

    next_button = (
        By.XPATH,
        "//button[text()='Siguiente']"
    )

    sms_code_field = (
        By.XPATH,
        "//input[@placeholder='Introduce el código']"
    )

    confirm_button = (
        By.XPATH,
        "//button[text()='Confirmar']"
    )

    payment_method = (
        By.CLASS_NAME,
        'pp-button'
    )

    add_card_button = (
        By.XPATH,
        "//div[text()='Agregar tarjeta']"
    )

    card_number_field = (
        By.ID,
        'number'
    )

    card_code_field = (
        By.ID,
        'code'
    )

    add_button = (
        By.XPATH,
        "//button[text()='Agregar']"
    )

    message_field = (
        By.ID,
        'comment'
    )

    blanket_switch = (
        By.CLASS_NAME,
        'switch-input'
    )

    icecream_plus = (
        By.CLASS_NAME,
        'counter-plus'
    )

    reserve_button = (
        By.CSS_SELECTOR,
        '.smart-button'
    )
    # INIT

    def __init__(self, driver):

        self.driver = driver

    # WAIT

    def wait_for_load_home_page(self):

        WebDriverWait(self.driver, 20).until(
            expected_conditions.presence_of_element_located(
                self.from_field
            )
        )

    # METHODS

    def set_from(self, from_address):

        self.driver.find_element(
            *self.from_field
        ).send_keys(from_address)

    def set_to(self, to_address):

        self.driver.find_element(
            *self.to_field
        ).send_keys(to_address)

    def set_route(self, from_address, to_address):

        self.set_from(from_address)

        self.set_to(to_address)

    def get_from(self):

        return self.driver.find_element(
            *self.from_field
        ).get_property('value')

    def get_to(self):

        return self.driver.find_element(
            *self.to_field
        ).get_property('value')

    def click_call_taxi_button(self):

        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(
                self.call_taxi_button
            )
        )

        self.driver.find_element(
            *self.call_taxi_button
        ).click()

    def click_comfort_rate(self):

        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(
                self.comfort_rate
            )
        )

        self.driver.find_element(
            *self.comfort_rate
        ).click()

    def set_phone_number(self, phone):

        self.driver.find_element(
            *self.phone_field
        ).send_keys(phone)

    def click_next_button(self):

        self.driver.find_element(
            *self.next_button
        ).click()

    def set_sms_code(self, code):

        self.driver.find_element(
            *self.sms_code_field
        ).send_keys(code)

    def click_confirm_button(self):

        self.driver.find_element(
            *self.confirm_button
        ).click()

    def click_payment_method(self):

        self.driver.find_element(
            *self.payment_method
        ).click()

    def click_add_card(self):

        self.driver.find_element(
            *self.add_card_button
        ).click()

    def set_card_number(self, number):

        self.driver.find_element(
            *self.card_number_field
        ).send_keys(number)

    def set_card_code(self, code):

        self.driver.find_element(
            *self.card_code_field
        ).send_keys(code)

    def click_add_button(self):

        self.driver.find_element(
            *self.add_button
        ).click()

    def set_message(self, message):

        self.driver.find_element(
            *self.message_field
        ).send_keys(message)

    def click_blanket_switch(self):

        self.driver.find_element(
            *self.blanket_switch
        ).click()

    def click_icecream_plus(self):

        self.driver.find_element(
            *self.icecream_plus
        ).click()

    def click_reserve_button(self):

        self.driver.find_element(
            *self.reserve_button
        ).click()