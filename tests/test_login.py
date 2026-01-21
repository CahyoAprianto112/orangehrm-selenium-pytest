from pages.login_page import LoginPage
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest

@pytest.mark.smoke
def test_login_success(driver): # login with valid credentials
    driver.implicitly_wait(20)
    login = LoginPage(driver)
    login.open()
    login.login("Admin", "admin123")
    time.sleep(5)
    
    assert "dashboard" in driver.current_url

def test_login_invalid_password(driver): # login with invalid password
    login = LoginPage(driver)
    
    login.open()
    login.login("Admin", "wrongpassword")
    error_text = login.get_alert_error()
    assert "Invalid credentials" in error_text
    time.sleep(5)
    driver.quit()

@pytest.mark.regression
def test_login_empty_username(driver): # login with empty username
    login = LoginPage(driver)
    login.open()
    login.login("", "admin123")
    error_text = login.get_required_error()
    time.sleep(5)
    assert "Required" in error_text

@pytest.mark.regression
def test_login_empty_username_and_password(driver): # login with empty username and password
    login = LoginPage(driver)
    login.open()
    login.login("", "")
    error_text = login.get_required_error()
    time.sleep(5)
    assert "Required" in error_text