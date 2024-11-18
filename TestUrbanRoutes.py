import data
from selenium import webdriver
from main import UrbanRoutesPage


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
        service = Service()

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

    def test_set_comfort_tariff(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_taxi_button()
        routes_page.set_comfort_tariff()
        assert 'Comfort' in routes_page.get_tariff_value()

    def test_set_phone_number(self):
        routes_page = UrbanRoutesPage(self.driver)
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
        assert routes_page.check_presence_of_taxi_modal()




    @classmethod
    def teardown_class(cls):
        cls.driver.quit()