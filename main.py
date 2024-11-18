from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from phone_code import retrieve_phone_code
import time


class UrbanRoutesPage:
    # Localizadores

    # localizadores para ingresar ruta
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    call_taxi_button = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[1]/div[3]/div[1]/button')
    comfort_tariff_button = (By.XPATH, './/div[@class = "tcard"]//div[contains(text(),"Comfort")]')
    active_tariff = (By.CSS_SELECTOR, '.tcard.active')

    # localizadores para ingresar número de teléfono
    phone_number_button = (By.CLASS_NAME, 'np-button')
    phone_number_field = (By.CSS_SELECTOR, '#phone')
    save_phone_number = (By.XPATH, './/div[@class = "buttons"]//button[contains(text(),"Siguiente")]')
    code_field = (By.XPATH, './/div[@class= "input-container"]//input[@id = "code"]')
    verify_code_button = (By.XPATH, '//*[text()="Confirmar"]')

    # localizadores para agregar tarjeta en Método de pago
    payment_method = (By.CLASS_NAME, 'pp-button')
    add_credit_card = (By.XPATH, '//*[text()="Agregar tarjeta"]')
    card_number_field = (By.ID, 'number')
    card_code_field = (By.CSS_SELECTOR, '#code.card-input')
    save_credit_card = (By.XPATH, '//div[@class="pp-buttons"]//button[contains(text(),"Agregar")]')
    change_focus = (By.CLASS_NAME, 'card-second-row')
    close_modal_button = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/button')

    # localizadores para agregar un mensaje y los requisitos del pedido
    message = (By.ID, 'comment')
    blanket_and_tissues_switch = (By.CLASS_NAME, 'r-sw')
    blanket_and_tissues_value = (By.XPATH, '//input[@class="switch-input"]')
    ice_cream_counter = (By.CLASS_NAME, 'counter-plus')
    ice_cream_number = (By.CLASS_NAME, 'counter-value')
    book_trip_button = (By.CLASS_NAME, 'smart-button')
    taxi_modal = (By.CLASS_NAME, 'order-body')

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

    # Elegir tarifa Comfort
    def set_comfort_tariff(self):
        self.driver.find_element(*self.comfort_tariff_button).click()
        time.sleep(3)

    def get_tariff_value(self):
        return self.driver.find_element(*self.active_tariff).text

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

    # Elegir método de pago
    def click_payment_method_button(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.payment_method))
        self.driver.find_element(*self.payment_method).click()
        time.sleep(3)

    # Agregar Tarjeta como otro método de pago
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

    # Hacer clic en otra parte del modal para que se habilite "Agregar"
    def click_on_screen(self):
        self.driver.find_element(*self.change_focus).click()
        time.sleep(2)

    # Guardar los datos de la tarjeta
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

    # Activar el switch de "Mantas y pañuelos"
    def turn_on_blanket_and_tissues(self):
        self.driver.find_element(*self.blanket_and_tissues_switch).click()
        time.sleep(3)

    # Revisar que el switch de Mantas y pañuelos esté seleccionado
    def check_blanket_switch_is_on(self):
        return self.driver.find_element(*self.blanket_and_tissues_value).is_selected()

    # Incrementar el contador de helado en 2
    def add_ice_cream_counter(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.ice_cream_counter))
        time.sleep(2)
        self.driver.find_element(*self.ice_cream_counter).click()
        time.sleep(2)
        self.driver.find_element(*self.ice_cream_counter).click()
        time.sleep(3)

    #Obtener el valor del contador de "Helado"
    def get_ice_cream_count(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.ice_cream_number))
        return int(self.driver.find_element(*self.ice_cream_number).text)

    #Reservar el taxi
    def click_book_trip_button(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.book_trip_button))
        self.driver.find_element(*self.book_trip_button).click()
        time.sleep(35)

    def check_presence_of_taxi_modal(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.taxi_modal))
        return True

    #Paso para establecer la ruta
    def set_route(self, from_field, to_field):
        self.set_from(from_field)
        self.set_to(to_field)

    #Paso para el proceso de Agregar número de teléfono
    def add_phone_number(self, phone_number):
        self.click_phone_number_button()
        self.set_phone_number(phone_number)
        self.click_save_phone_number_button()
        code = retrieve_phone_code(self.driver)
        self.set_verification_code(code)
        self.click_verify_code_button()

    #Paso para el proceso de agregar Método de pago
    def add_payment_method(self, card_number, card_code):
        self.click_payment_method_button()
        self.add_credit_card_button()
        self.set_card_number(card_number)
        self.set_card_code(card_code)
        self.click_on_screen()
        self.click_save_card_button()
        self.click_close_payment_method_modal()
