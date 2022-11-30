import re
import time

from Library.excel_lib import ReadExcel
from Library.configuration import Configuration
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select



class HotelModule:
    obj_1 = ReadExcel()
    locator_hotel = obj_1.read_locator(Configuration.HOTEL_MODULE_LOCATOR_SHEET)

    def __init__(self, driver):
        self.driver = driver
        self.action_obj = ActionChains(driver)

    def click_hotel_btn(self):
        locator = self.locator_hotel["hotel_link"]
        self.driver.find_element(*locator).click()

    def click_india_radio_btn(self):
        locator = self.locator_hotel["india_radio_btn"]
        self.driver.find_element(*locator).click()

    def click_international_radio_btn(self):
        locator = self.locator_hotel["international_radio_btn"]
        self.driver.find_element(*locator).click()

    def enter_where_txt(self, where_text):
        locator = self.locator_hotel["where_txt"]
        self.driver.find_element(*locator).send_keys(where_text)
        time.sleep(2)
        self.action_obj.key_down(Keys.ARROW_DOWN).perform()
        self.action_obj.key_down(Keys.ENTER).perform()

    def select_dates(self):
        locator = self.locator_hotel["check_in_calender"]
        self.driver.find_element(*locator).click()
        # time.sleep(2)
        self.driver.implicitly_wait(10)
        locator = self.locator_hotel["check_in_date"]
        self.driver.find_element(*locator).click()
        # time.sleep(2)
        self.driver.implicitly_wait(10)
        locator = self.locator_hotel["check_out_date"]
        self.driver.find_element(*locator).click()

    def select_guest_and_rooms(self):
        locator = self.locator_hotel["guests_rooms"]
        self.driver.find_element(*locator).click()
        time.sleep(1)
        self.driver.implicitly_wait(10)
        locator = self.locator_hotel["increase_rooms"]
        self.driver.find_element(*locator).click()
        time.sleep(1)
        locator = self.locator_hotel["decrease_rooms"]
        self.driver.find_element(*locator).click()
        self.driver.implicitly_wait(10)
        locator = self.locator_hotel["click_on_done"]
        self.driver.find_element(*locator).click()


    def click_on_search(self):
        locator = self.locator_hotel["search_btn"]
        self.driver.find_element(*locator).click()
        time.sleep(3)

    def select_hotel(self):

        locator = self.locator_hotel["click_hotel"]
        self.driver.find_element(*locator).click()


    def select_room(self):
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[1])
        self.driver.implicitly_wait(10)
        locator = self.locator_hotel["click_on_view_options"]
        self.driver.find_element(*locator).click()
        time.sleep(2)
        locator = self.locator_hotel["select_room"]
        self.driver.find_element(*locator).click()
        locator = self.locator_hotel["click_on_dropdown"]
        self.driver.find_element(*locator).click()

        locator = self.locator_hotel["click_on_miss"]
        list_box1 = self.driver.find_element(*locator)
        time.sleep(1)

    def enter_first_name(self, first_name):
        locator = self.locator_hotel["enter_FirstName"]
        result = re.findall('[a-zA-Z]', first_name)
        assert result, "invalid first_name"
        self.driver.find_element(*locator).send_keys(first_name)

    def enter_last_name(self, last_name):
        locator = self.locator_hotel["enter_LastName"]
        result = re.findall('[a-zA-Z]', last_name)
        assert result, "invalid last_name"
        self.driver.find_element(*locator).send_keys(last_name)

    def enter_email_id(self, Email_id):
        locator = self.locator_hotel["enter_Email"]
        result = re.findall(r"\w+@gmail\.com", Email_id)
        assert result != [], "invalid email_id"
        self.driver.find_element(*locator).send_keys(Email_id)

    def select_countrycode(self):
        locator = self.locator_hotel["enter_country_code"]
        list_box2 = self.driver.find_element(*locator)
        s_obj = Select(list_box2)
        # s_obj.select_by_visible_text("+247 Ascension Island")
        s_obj.select_by_visible_text("+91 India")
        time.sleep(1)

    def enter_mb_num(self, enter_Phno):
        if isinstance(enter_Phno, float):
            enter_Phno = str(int(enter_Phno))
        assert len(enter_Phno) == 10, "invaild mb_num"
        locator = self.locator_hotel["enter_Phno"]
        self.driver.find_element(*locator).send_keys(enter_Phno)









