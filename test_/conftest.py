import pytest
from selenium import webdriver
from Library.configuration import Configuration


@pytest.fixture(params=["Chrome"])
def init_driver(request):
    global driver
    # browser = request.param

    if request.param == "Chrome":
        driver = webdriver.Chrome(executable_path=Configuration.CHROME_PATH)

    elif request.param == "Edge":
         driver = webdriver.Edge(executable_path=Configuration.MSEDGE_PATH)




    driver.get(Configuration.URL)
    driver.implicitly_wait(30)
    driver.maximize_window()
    yield driver

    path=r"C:\Users\V.Aparna\PycharmProjects\goibibo_hotels\screenshot\\"
    driver.save_screenshot(path+"Room_booking.png")
    driver.quit()
