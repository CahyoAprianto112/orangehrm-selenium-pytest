import pytest
from utils.driver_setup import get_driver

@pytest.fixture
def driver():
    driver = get_driver("edge") 
    driver.maximize_window()
    yield driver
    driver.quit()