import time

import pytest
import datetime
from Library.configuration import Configuration
from Library.excel_lib import ReadExcel
from POM.hotel_module import HotelModule


class TestHotelModule:
    obj = ReadExcel()
    data = obj.read_test_data(Configuration.HOTEL_MODULE_TESTDATA_SHEET)

    @pytest.mark.parametrize("where_text, first_name, last_name, email_id, mb_num", data)
    def test_hotel_module(self,init_driver, where_text,first_name, last_name, email_id, mb_num):
        driver = init_driver

        hm = HotelModule(driver)
        hm.click_hotel_btn()
        hm.click_international_radio_btn()
        hm.enter_where_txt(where_text)
        hm.select_dates()
        hm.select_guest_and_rooms()
        hm.click_on_search()
        hm.select_hotel()
        hm.select_room()
        hm.enter_first_name(first_name)
        hm.enter_last_name(last_name)
        hm.enter_email_id(email_id)
        hm.enter_mb_num(mb_num)







