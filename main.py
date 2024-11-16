import data
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

from data import phone_number, card_number


# no modificar
def retrieve_phone_code(driver) -> str:
    """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string.
    Utilízalo cuando la aplicación espere el código de confirmación para pasarlo a tus pruebas.
    El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación."""

    import json
    import time
    from selenium.common import WebDriverException
    code = None
    for i in range(10):
        try:
            logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                    and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
        except WebDriverException:
            time.sleep(1)
            continue
        if not code:
            raise Exception("No se encontró el código de confirmación del teléfono.\n"
                            "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación.")
        return code


class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    call_taxi_button = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[1]/div[3]/div[1]/button')
    comfort_tariff_button = (By.XPATH, './/div[@class = "tcard"]//div[contains(text(),"Comfort")]')

    phone_number_button = (By.CLASS_NAME, 'np-button')
    phone_number_field = (By.CSS_SELECTOR, '#phone')
    save_phone_number = (By.XPATH, './/div[@class = "buttons"]//button[contains(text(),"Siguiente")]')
    code_field = (By.XPATH, './/div[@class= "input-container"]//input[@id = "code"]')
    verify_code_button = (By.XPATH, '//*[text()="Confirmar"]')

    payment_method = (By.CLASS_NAME, 'pp-button')
    add_credit_card = (By.XPATH, '//*[text()="Agregar tarjeta"]')
    card_number_field = (By.ID, 'number')
    card_code_field = (By.CSS_SELECTOR, '#code.card-input')
    save_credit_card = (By.XPATH, '//div[@class="pp-buttons"]//button[contains(text(),"Agregar")]')
    change_focus = (By.CLASS_NAME, 'card-second-row')
    close_modal_button = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/button')

    message = (By.ID, 'comment')
    blanket_and_tissues_switch = (By.CLASS_NAME, 'r-sw')
    blanket_and_tissues_value = (By.XPATH, '//input[@class="switch-input"]')
    ice_cream_counter = (By.CLASS_NAME, 'counter-plus')
    ice_cream_number = (By.CLASS_NAME, 'counter-value')
    book_trip_button = (By.CLASS_NAME, 'smart-button')


    def __init__(self, driver):
        self.driver = driver

    def set_from(self, from_address):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.from_field))
        time.sleep(5)
        self.driver.find_element(*self.from_field).send_keys(from_address)
        time.sleep(3)

    def set_to(self, to_address):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.to_field))
        time.sleep(5)
        self.driver.find_element(*self.to_field).send_keys(to_address)
        time.sleep(5)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def set_comfort_tariff(self):
        self.driver.find_element(*self.comfort_tariff_button).click()
        time.sleep(3)

    def click_taxi_button(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.call_taxi_button))
        time.sleep(3)
        self.driver.find_element(*self.call_taxi_button).click()
        time.sleep(3)

    def click_phone_number_button(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.phone_number_button))
        self.driver.find_element(*self.phone_number_button).click()
        time.sleep(3)

    def set_phone_number(self, phone_number):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.phone_number_field))
        self.driver.find_element(*self.phone_number_field).send_keys(phone_number)
        time.sleep(3)

    def get_phone_number(self):
        return self.driver.find_element(*self.phone_number_field).get_property('value')

    def click_save_phone_number_button(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.save_phone_number))
        self.driver.find_element(*self.save_phone_number).click()
        time.sleep(3)

    def set_verification_code(self, code):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.code_field))
        self.driver.find_element(*self.code_field).send_keys(code)
        time.sleep(3)

    def get_verification_code(self):
        return self.driver.find_element(*self.code_field).get_property('value')

    def click_verify_code_button(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.verify_code_button))
        self.driver.find_element(*self.verify_code_button).click()
        time.sleep(3)

    def click_payment_method_button(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.payment_method))
        self.driver.find_element(*self.payment_method).click()
        time.sleep(3)

    def add_credit_card_button(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.add_credit_card))
        self.driver.find_element(*self.add_credit_card).click()
        time.sleep(3)

    def set_card_number(self, card_number):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.card_number_field))
        self.driver.find_element(*self.card_number_field).send_keys(card_number)
        time.sleep(3)

    def set_card_code(self, card_code):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.card_code_field))
        self.driver.find_element(*self.card_code_field).send_keys(card_code)
        time.sleep(3)

    def get_card_number(self):
        return self.driver.find_element(*self.card_number_field).get_property('value')

    def get_card_code(self):
        return self.driver.find_element(*self.card_code_field).get_property('value')

    def click_on_screen(self):   #hacer clic en tab u otra parte del modal para que se habilite Agregar
        self.driver.find_element(*self.change_focus).click()
        time.sleep(2)

    def click_save_card_button(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.save_credit_card))
        self.driver.find_element(*self.save_credit_card).click()
        time.sleep(3)

    def click_close_payment_method_modal(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.close_modal_button))
        self.driver.find_element(*self.close_modal_button).click()
        time.sleep(3)

    def set_driver_message(self, comment):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.message))
        self.driver.find_element(*self.message).send_keys(comment)
        time.sleep(3)

    def get_driver_message(self):
        return self.driver.find_element(*self.message).get_property('value')

    def turn_on_blanket_and_tissues(self):
        self.driver.find_element(*self.blanket_and_tissues_switch).click()
        time.sleep(3)

    def check_blanket_switch_is_on(self):
        return self.driver.find_element(*self.blanket_and_tissues_value).is_selected()

    def add_ice_cream_counter(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.ice_cream_counter))
        time.sleep(2)
        self.driver.find_element(*self.ice_cream_counter).click()
        time.sleep(2)
        self.driver.find_element(*self.ice_cream_counter).click()
        time.sleep(3)

    def get_ice_cream_count(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.ice_cream_number))
        return int(self.driver.find_element(*self.ice_cream_number).text)

    def click_book_trip_button(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.book_trip_button))
        self.driver.find_element(*self.book_trip_button).click()
        time.sleep(35)

    def set_route(self, from_field, to_field):
        self.set_from(from_field)
        self.set_to(to_field)

    def add_phone_number(self, phone_number):
        self.click_phone_number_button()
        self.set_phone_number(phone_number)
        self.click_save_phone_number_button()
        code = retrieve_phone_code(self.driver)
        self.set_verification_code(code)
        self.click_verify_code_button()

    def add_payment_method(self, card_number, card_code):
        self.click_payment_method_button()
        self.add_credit_card_button()
        self.set_card_number(card_number)
        self.set_card_code(card_code)
        self.click_on_screen()
        self.click_save_card_button()
        self.click_close_payment_method_modal()


class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        from selenium.webdriver.chrome.service import Service
        from selenium.webdriver.chrome.options import Options
        # Configurar las opciones del navegador
        options = Options()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        options.set_capability("goog:loggingPrefs", {"performance": "ALL"})

        # Iniciar el servicio de Chrome
        service = Service()  # Puedes pasar el path del driver aquí si es necesario

        # Inicializar el driver con opciones
        cls.driver = webdriver.Chrome(service=service, options=options)


    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    def test_set_phone_number(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_taxi_button()
        routes_page.set_comfort_tariff()
        phone_number = data.phone_number
        routes_page.add_phone_number(phone_number)
        assert routes_page.get_phone_number() == phone_number


    def test_set_payment_method(self):
        routes_page = UrbanRoutesPage(self.driver)
        card_number = data.card_number
        card_code = data.card_code
        routes_page.add_payment_method(card_number, card_code)
        assert routes_page.get_card_number() == card_number
        assert routes_page.get_card_code() == card_code

    def test_set_driver_message(self):
        routes_page = UrbanRoutesPage(self.driver)
        message = data.message_for_driver
        routes_page.set_driver_message(message)
        assert routes_page.get_driver_message() == message

    def test_check_blanket_switch_is_on(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.turn_on_blanket_and_tissues()
        assert routes_page.check_blanket_switch_is_on()

    def test_get_ice_cream_count(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.add_ice_cream_counter()
        assert routes_page.get_ice_cream_count() == 2

    def test_book_trip_button(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_book_trip_button()



    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
