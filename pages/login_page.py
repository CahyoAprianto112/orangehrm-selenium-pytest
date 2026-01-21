from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        self.username_input = (By.NAME, "username")
        self.password_input = (By.NAME, "password")
        self.login_button = (By.XPATH, "//button[@type='submit']")
        # error invalid credential (alert)
        self.alert_error = (
            By.XPATH, "//p[contains(@class,'oxd-alert-content-text')]"
        )
        # error required (inline)
        self.required_error = (
            By.XPATH, "//span[contains(@class,'oxd-input-field-error-message')]"
        )

    def open(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")

    def login(self, username, password):
        self.wait.until(EC.visibility_of_element_located(self.username_input)).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()

    def get_alert_error(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.alert_error)
        ).text

    def get_required_error(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.required_error)
        ).text
