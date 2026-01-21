from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class PersonalDetailsPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

        self.last_name_input = (By.NAME, "lastName")
        self.save_button = (By.XPATH, "//button[@type='submit']")
        self.success_toast = (By.XPATH, "//div[contains(@class,'oxd-toast-content')]")
        self.form_loader = (By.XPATH, "//div[contains(@class,'oxd-form-loader')]")

    def update_last_name(self, new_last_name):
        self.wait.until(EC.invisibility_of_element_located(self.form_loader))

        field = self.wait.until(EC.element_to_be_clickable(self.last_name_input))

        # HAPUS TOTAL ISI FIELD
        field.click()
        field.send_keys(Keys.CONTROL, "a")
        field.send_keys(Keys.DELETE)

        # INPUT BARU
        field.send_keys(new_last_name)

        save_btn = self.wait.until(EC.element_to_be_clickable(self.save_button))
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});", save_btn
        )
        save_btn.click()

        self.wait.until(EC.visibility_of_element_located(self.success_toast))

    def get_toast_message(self):
        wait = WebDriverWait(self.driver, 10)
        toast = wait.until(EC.visibility_of_element_located(self.success_toast))
        return toast.text

    def wait_until_loaded(self):
        self.wait.until(EC.visibility_of_element_located(self.last_name_input))
